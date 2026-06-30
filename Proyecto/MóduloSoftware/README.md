# Yaku-Ñawi · Guía de integración YOLOv8 + ESP32-S3

## Estructura del proyecto

```
yaku-nawi/
├── app.py                  ← Servidor Flask + YOLOv8 (ejecutar en la PC)
├── best.pt                 ← Tu modelo YOLOv8 entrenado (colocar aquí)
├── esp32_yaku_nawi.ino     ← Código Arduino para el ESP32-S3 XIAO Sense
├── templates/
│   └── index.html          ← Dashboard web (sirve Flask automáticamente)
├── static/
│   └── ultima.jpg          ← Último frame recibido del ESP32 (auto-generado)
└── README.md
```

---

## 1. Instalar dependencias en la PC

```bash
pip install flask ultralytics opencv-python numpy
```

---

## 2. Colocar el modelo YOLOv8

Copia tu archivo `best.pt` (entrenado con PET y EPS) a la raíz del proyecto.  
Si no tienes `best.pt` aún, Flask usará `yolov8n.pt` como fallback (sin clases de microplásticos).

---

## 3. Correr el servidor

```bash
cd yaku-nawi/
python app.py
```

Verás:
```
  Yaku-Ñawi · Servidor Flask + YOLOv8
  Escuchando en http://0.0.0.0:5000
  Dashboard → http://localhost:5000
  ESP32 POST → http://<TU_IP>:5000/detect
```

Abre el navegador en `http://localhost:5000`.

---

## 4. Configurar el ESP32-S3 XIAO Sense

En el archivo `esp32_yaku_nawi.ino`, edita:

```cpp
const char* SSID     = "TU_RED_WIFI";      // nombre de tu red
const char* PASSWORD = "TU_PASSWORD_WIFI"; // contraseña
const char* FLASK_URL = "http://192.168.1.100:5000/detect";
//                              ↑ IP de la PC donde corre Flask
```

**¿Cómo obtener la IP de la PC?**
- Windows: `ipconfig` → busca "Dirección IPv4"
- Linux/Mac: `ifconfig` o `ip addr`

Asegúrate de que la PC y el ESP32 estén en **la misma red WiFi**.

---

## 5. Subir el sketch al ESP32-S3 XIAO Sense

1. Arduino IDE → Board Manager → instala "esp32 by Espressif Systems"
2. Selecciona la placa: `Tools → Board → XIAO_ESP32S3`
3. Abre `esp32_yaku_nawi.ino`, edita SSID/PASSWORD/FLASK_URL
4. Sube el sketch
5. Abre el Monitor Serie a 115200 baudios para ver los logs

---

## 6. Flujo de datos completo

```
ESP32-S3 XIAO Sense
  │  (OV2640 captura frame JPEG)
  │  (sensor turbidez → NTU)
  │  (sensor TDS → µS/cm)
  │
  │  HTTP POST /detect
  │  Headers: Turbidez: <NTU>, TDS: <µS/cm>
  │  Body: bytes JPEG
  ▼
Flask (app.py) en la PC
  │  Guarda imagen en static/ultima.jpg
  │  Decodifica imagen con OpenCV
  │  Corre inferencia YOLOv8 (best.pt)
  │  Parsea detecciones PET / EPS
  │  Guarda resultado en último_resultado
  ▼
Dashboard (index.html)
  │  Polling GET /datos cada 3 segundos
  │  Muestra imagen, objetos, barras, sparklines
  └  Actualiza historial y tabla
```

---

## 7. Endpoints disponibles

| Endpoint    | Método | Descripción |
|-------------|--------|-------------|
| `/`         | GET    | Dashboard web |
| `/datos`    | GET    | JSON con último resultado + historial |
| `/detect`   | POST   | Recibe imagen + headers del ESP32 |
| `/status`   | GET    | Estado del servidor y modelo |

---

## 8. Ajustar clases del modelo

En `app.py`, si tus clases tienen nombres diferentes a `pet`/`eps`, edita:

```python
count_pet = sum(1 for o in objetos_detectados if "pet" in o.lower())
count_eps = sum(1 for o in objetos_detectados if "eps" in o.lower())
```

Por ejemplo, si tu modelo usa `microplastico_pet` y `microplastico_eps`, ya funciona porque usa `in o.lower()`.

---

## Notas

- El ESP32-S3 XIAO Sense incluye cámara **OV3660** y módulo WiFi integrado.  
- La resolución **QVGA (320×240)** equilibra velocidad de transferencia y precisión del modelo.  
- Para pruebas sin ESP32, puedes hacer un POST manual con `curl`:

```bash
curl -X POST http://localhost:5000/detect \
  -H "Turbidez: 45.2" \
  -H "TDS: 320" \
  -H "Content-Type: image/jpeg" \
  --data-binary @foto_muestra.jpg
```
