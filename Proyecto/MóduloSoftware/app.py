"""
Yaku-Ñawi · Backend Flask + YOLOv8  ·  v2 (Live Stream)
=========================================================
CAMBIOS respecto al app.py original del zip:
  1. Nuevo endpoint POST /frame  → recibe frames del ESP32 para el stream
  2. Nuevo endpoint GET /video_feed → emite MJPEG al <img> del dashboard
  3. Hilo background YOLO → procesa frames sin bloquear Flask
  4. Guardado automático de capturas en static/capturas/YYYYMMDD_HHMMSS.jpg
  5. MQTT HiveMQ Cloud privado con TLS (reemplaza broker público)
  6. /datos actualizado para el nuevo dashboard con /video_feed

El endpoint /detect original se mantiene por compatibilidad.

pip install flask ultralytics opencv-python numpy paho-mqtt
"""

import threading
import time
import ssl
import os
from datetime import datetime
from collections import deque

import cv2
import numpy as np
from flask import Flask, Response, request, jsonify, render_template
from ultralytics import YOLO
import paho.mqtt.client as mqtt

app = Flask(__name__)

# ══════════════════════════════════════════════════════════════
#  MODELO YOLOv8
# ══════════════════════════════════════════════════════════════
MODEL_PATH = "best.pt"
if not os.path.exists(MODEL_PATH):
    print(f"[WARN] {MODEL_PATH} no encontrado → probando yolov8n.pt")
    MODEL_PATH = "yolov8n.pt"

modelo = YOLO(MODEL_PATH)
print(f"[OK] Modelo: {MODEL_PATH}")
print(f"[OK] Clases: {modelo.names}")

# ══════════════════════════════════════════════════════════════
#  CARPETA DE CAPTURAS JPEG
#  Las imágenes se guardan en static/capturas/ con timestamp.
#  Accesibles desde el browser en /static/capturas/nombre.jpg
# ══════════════════════════════════════════════════════════════
CAPTURAS_DIR = os.path.join("static", "capturas")
os.makedirs(CAPTURAS_DIR, exist_ok=True)
MAX_CAPTURAS = 100   # máximo de archivos guardados (borra los más viejos)

def guardar_captura(jpeg_bytes):
    """
    Guarda un JPEG en static/capturas/YYYYMMDD_HHMMSS_mmm.jpg
    Si hay más de MAX_CAPTURAS archivos, elimina los más viejos.
    """
    ts  = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
    ruta = os.path.join(CAPTURAS_DIR, f"{ts}.jpg")
    with open(ruta, "wb") as f:
        f.write(jpeg_bytes)

    # Limpieza automática: mantiene solo los últimos MAX_CAPTURAS archivos
    archivos = sorted(
        [os.path.join(CAPTURAS_DIR, x) for x in os.listdir(CAPTURAS_DIR)
         if x.endswith(".jpg")],
        key=os.path.getmtime
    )
    while len(archivos) > MAX_CAPTURAS:
        os.remove(archivos.pop(0))

    return ruta

# ══════════════════════════════════════════════════════════════
#  MQTT  (HiveMQ Cloud privado + TLS)
#  Si prefieres el broker público sin TLS, comenta el bloque
#  tls_set y cambia MQTT_PORT a 1883.
# ══════════════════════════════════════════════════════════════
MQTT_BROKER   = "2d91ed0f7c114a8cac84ad4e8606c27e.s1.eu.hivemq.cloud"
MQTT_PORT     = 8883
MQTT_USER     = "engineerbk4"
MQTT_PASSWORD = "kimnamjoonDay6"
TOPIC_TURB    = "yakuawi/turbidez"
TOPIC_TDS     = "yakuawi/tds"

# ══════════════════════════════════════════════════════════════
#  ESTADO GLOBAL  (thread-safe)
# ══════════════════════════════════════════════════════════════
lock = threading.Lock()

# frame_buffer: bytes JPEG crudos del ESP32 (el más reciente)
# annotated_buffer: bytes JPEG con bboxes de YOLO dibujadas
frame_buffer     = None
annotated_buffer = None

datos_sensores = {"turbidez": 0.0, "tds": 0.0, "ts": ""}

ultimo_resultado = {
    "objetos":     [],
    "cantidad":    0,
    "turbidez":    0.0,
    "tds":         0.0,
    "pet":         0,
    "eps":         0,
    "confianza":   0.0,
    "timestamp":   "",
    "latencia_ms": 0,
    "imagen_ok":   False,
    "modelo":      MODEL_PATH
}

historial    = deque(maxlen=50)
MAX_HISTORIAL = 50

# ══════════════════════════════════════════════════════════════
#  HILO YOLO  —  procesa frames en background
#  Toma el frame_buffer, corre inferencia, dibuja bboxes,
#  actualiza annotated_buffer y ultimo_resultado.
# ══════════════════════════════════════════════════════════════
def yolo_worker():
    global frame_buffer, annotated_buffer, ultimo_resultado

    while True:
        with lock:
            raw = frame_buffer

        if raw is None:
            time.sleep(0.05)
            continue

        # Decodificar JPEG → numpy
        nparr = np.frombuffer(raw, np.uint8)
        img   = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            time.sleep(0.05)
            continue

        # Inferencia YOLOv8
        t0         = time.time()
        resultados = modelo(img, verbose=False)
        latencia   = round((time.time() - t0) * 1000, 1)

        # Imagen anotada con bboxes (devuelve numpy BGR)
        img_ann = resultados[0].plot()

        # Parsear detecciones
        objetos, confianzas = [], []
        for r in resultados:
            for box in r.boxes:
                objetos.append(modelo.names[int(box.cls)])
                confianzas.append(float(box.conf))

        total   = len(objetos)
        cnt_pet = objetos.count("PET")
        cnt_eps = objetos.count("EPS")

        pct_pet = round(cnt_pet / total * 100) if total else 0
        pct_eps = round(cnt_eps / total * 100) if total else 0

        conf_prom = round(sum(confianzas) / total * 100, 1) if total else 0.0

        ts = datetime.now().strftime("%H:%M:%S")

        tipo_dominante = objetos[0] if objetos else "Sin detecciones"

        # Codificar imagen anotada a JPEG para el stream
        _, jpeg = cv2.imencode(".jpg", img_ann,
                               [cv2.IMWRITE_JPEG_QUALITY, 80])

        with lock:
            annotated_buffer = jpeg.tobytes()
            s = datos_sensores
            ultimo_resultado = {
                "objetos": objetos,
                "cantidad": total,
                "tipo": tipo_dominante,
                "turbidez": s["turbidez"],
                "tds": s["tds"],
                "pet": pct_pet,
                "eps": pct_eps,
                "confianza": conf_prom,
                "timestamp": ts,
                "latencia_ms": latencia,
                "imagen_ok": True,
                "modelo": MODEL_PATH
            }
            historial.append({
                "time": ts,
                "tipo": tipo_dominante,
                "turbidez": s["turbidez"],
                "tds": s["tds"],
                "pet": pct_pet,
                "eps": pct_eps,
                "confianza": conf_prom
            })

        time.sleep(0.02)   # ~50 inferencias/s máx; ajusta si la CPU va al 100%

# Lanzar hilo YOLO al importar
threading.Thread(target=yolo_worker, daemon=True).start()

# ══════════════════════════════════════════════════════════════
#  MQTT CALLBACKS
# ══════════════════════════════════════════════════════════════
def on_connect(client, userdata, flags, rc):
    msgs = {0:"OK", 4:"Credenciales incorrectas", 5:"No autorizado"}
    print(f"[MQTT] Conexión: {msgs.get(rc, rc)}")
    if rc == 0:
        client.subscribe(TOPIC_TURB)
        client.subscribe(TOPIC_TDS)
        print(f"[MQTT] Suscrito a {TOPIC_TURB} | {TOPIC_TDS}")

def on_message(client, userdata, msg):
    try:
        valor = float(msg.payload.decode().strip())
    except ValueError:
        return
    with lock:
        if msg.topic == TOPIC_TURB:
            datos_sensores["turbidez"] = round(valor, 2)
        elif msg.topic == TOPIC_TDS:
            datos_sensores["tds"] = round(valor, 2)
        datos_sensores["ts"] = datetime.now().strftime("%H:%M:%S")
    print(f"[MQTT] {msg.topic.split('/')[-1]} = {valor:.2f}")

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"[MQTT] Desconexión inesperada rc={rc}")

# ══════════════════════════════════════════════════════════════
#  RUTAS FLASK
# ══════════════════════════════════════════════════════════════

@app.route("/")
def home():
    return render_template("index.html")


# ── /frame  ·  NUEVO  ─────────────────────────────────────────
@app.route("/frame", methods=["POST"])
def recibir_frame():
    """
    El ESP32 hace POST de cada JPEG aquí (cada 150 ms ≈ 6 fps).
    Flask mete el frame en el buffer y responde 200 inmediatamente
    para no frenar al ESP32. El hilo YOLO procesa en background.

    También guarda una captura en disco cada 10 s para el historial.
    """
    global frame_buffer

    raw = request.data
    print("Frame recibido:", len(raw))
    if not raw:
        return "", 400

    # Actualizar sensores desde headers (si el ESP32 los manda)
    try:
        t = float(request.headers.get("Turbidez", 0) or 0)
        s = float(request.headers.get("TDS",      0) or 0)
        with lock:
            if t: datos_sensores["turbidez"] = round(t, 2)
            if s: datos_sensores["tds"]      = round(s, 2)
            datos_sensores["ts"] = datetime.now().strftime("%H:%M:%S")
    except (ValueError, TypeError):
        pass

    with lock:
        frame_buffer = raw
        print("Frame guardado")

    # Guardar captura en disco cada 10 s para conservar historial de imágenes.
    # Se guarda el JPEG crudo (sin anotaciones) para auditoría.
    if not hasattr(recibir_frame, "_last_save"):
        recibir_frame._last_save = 0
    now = time.time()
    if now - recibir_frame._last_save >= 10:
        recibir_frame._last_save = now
        threading.Thread(
            target=guardar_captura, args=(raw,), daemon=True
        ).start()

    return "", 200


# ── /video_feed  ·  NUEVO  ───────────────────────────────────
def _generar_mjpeg():
    """
    Generador infinito de frames MJPEG.
    El browser los consume como <img src="/video_feed">.
    Si no hay frame todavía muestra una pantalla de espera.
    """
    placeholder = None   # se genera una sola vez

    while True:
        with lock:
            jpeg = annotated_buffer

        if jpeg is None:
            # Generar placeholder solo la primera vez
            if placeholder is None:
                img = np.zeros((240, 320, 3), dtype=np.uint8)
                cv2.putText(img, "Esperando camara...",
                            (30, 120), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 200, 100), 2)
                _, enc  = cv2.imencode(".jpg", img)
                placeholder = enc.tobytes()
            jpeg = placeholder

        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n"
               + jpeg
               + b"\r\n")
        time.sleep(0.05)   # 20 fps máx al cliente


@app.route("/video_feed")
def video_feed():
    """Stream MJPEG — se usa como <img src='/video_feed'>"""
    return Response(
        _generar_mjpeg(),
        mimetype="multipart/x-mixed-replace; boundary=frame"
    )


# ── /datos  ·  actualizado para el nuevo dashboard ────────────
@app.route("/datos")
def datos():
    with lock:
        res  = dict(ultimo_resultado)
        sens = dict(datos_sensores)
        hist = list(historial)[-8:]

    # Inyectar sensores actuales en el resultado
    res["turbidez"] = sens["turbidez"]
    res["tds"]      = sens["tds"]

    return jsonify({
        "ultimo":    res,      # compatibilidad con JS original del zip
        "historial": hist,
        "sensores":  sens      # nuevo campo para el dashboard v2
    })


# ── /detect  ·  ORIGINAL conservado por compatibilidad ────────
@app.route("/detect", methods=["POST"])
def detect():
    """
    Endpoint original. Redirige al nuevo flujo /frame internamente.
    Si alguien tiene el ino antiguo apuntando a /detect, sigue funcionando.
    """
    global frame_buffer, ultimo_resultado, historial

    try:
        turbidez = float(request.headers.get("Turbidez", 0))
    except (ValueError, TypeError):
        turbidez = 0.0
    try:
        tds = float(request.headers.get("TDS", 0))
    except (ValueError, TypeError):
        tds = 0.0

    imagen_bytes = request.data
    if not imagen_bytes:
        return jsonify({"status": "ok_sin_imagen"}), 200

    # Guardar última imagen estática para compatibilidad
    os.makedirs("static", exist_ok=True)
    with open("static/ultima.jpg", "wb") as f:
        f.write(imagen_bytes)

    # Meter en el buffer para que el stream y YOLO lo procesen
    with lock:
        frame_buffer = imagen_bytes
        datos_sensores["turbidez"] = round(turbidez, 2)
        datos_sensores["tds"]      = round(tds, 2)

    # Dar tiempo al hilo YOLO para procesar (máx 2s)
    deadline = time.time() + 2.0
    while time.time() < deadline:
        with lock:
            res = dict(ultimo_resultado)
        if res["imagen_ok"]:
            break
        time.sleep(0.05)

    return jsonify(res)


# ── /capturas  ·  NUEVO  ─────────────────────────────────────
@app.route("/capturas")
def listar_capturas():
    """
    Devuelve la lista de capturas guardadas en disco.
    Útil para un futuro visor de historial de imágenes.
    """
    archivos = sorted(
        [f for f in os.listdir(CAPTURAS_DIR) if f.endswith(".jpg")],
        reverse=True
    )[:20]   # últimas 20
    urls = [f"/static/capturas/{f}" for f in archivos]
    return jsonify({"capturas": urls, "total": len(archivos)})


# ══════════════════════════════════════════════════════════════
#  ARRANQUE
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":

    # MQTT con TLS (HiveMQ Cloud privado)
    mq = mqtt.Client(client_id="YakuNawi-Flask", protocol=mqtt.MQTTv311)
    mq.username_pw_set(MQTT_USER, MQTT_PASSWORD)
    mq.tls_set(ca_certs=None, tls_version=ssl.PROTOCOL_TLS,
               cert_reqs=ssl.CERT_REQUIRED)
    mq.tls_insecure_set(False)
    mq.on_connect    = on_connect
    mq.on_message    = on_message
    mq.on_disconnect = on_disconnect

    try:
        mq.connect(MQTT_BROKER, MQTT_PORT, keepalive=60)
        mq.loop_start()
        print(f"[MQTT] Conectando a {MQTT_BROKER}:{MQTT_PORT} ...")
    except Exception as e:
        print(f"[MQTT] No se pudo conectar: {e} (el resto funciona igual)")

    print("=" * 58)
    print("  Yaku-Ñawi · Flask v2  ·  Live Stream + YOLOv8")
    print("  Dashboard    →  http://localhost:5000")
    print("  Stream       →  http://localhost:5000/video_feed")
    print("  Frames in    →  POST http://10.108.103.206:5000/frame")
    print("  Capturas     →  http://localhost:5000/capturas")
    print(f"  MQTT TLS     →  {MQTT_BROKER}:{MQTT_PORT}")
    print(f"  JPEGs        →  {os.path.abspath(CAPTURAS_DIR)}/")
    print("=" * 58)

    # threaded=True es OBLIGATORIO para servir el MJPEG y el polling a la vez
    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)