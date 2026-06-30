#include <Arduino.h>
#include "esp_camera.h"
#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// ===========================
// Select camera model in board_config.h
// ===========================
#include "board_config.h"

// ===========================
// Enter your WiFi credentials
// ===========================
const char *ssid = "Redmi 13C";
const char *password = "12345678";
const char *FLASK_URL_FRAME    = "http://10.108.103.206:5000/frame";
const char *FLASK_URL_SENSORES = "http://10.108.103.206:5000/sensores";

//=========================
// MODO DE PRUEBA
// Pon en 1 para probar rapido (ciclo de LED de 5 s),
// pon en 0 para el funcionamiento real (ciclo de 2 min).
//=========================
#define MODO_PRUEBA 1

#if MODO_PRUEBA
  const unsigned long TIEMPO_LED = 5000;   // 5 segundos (PRUEBA)
#else
  const unsigned long TIEMPO_LED = 120000; // 2 minutos (REAL)
#endif

//=========================
// Si quieres ademas levantar el servidor de streaming
// nativo del ESP32 (ademas de mandar frames a Flask), pon esto en 1.
// Para tu objetivo actual (comprobar LCD/LEDs/sensores en la web Flask)
// puedes dejarlo en 0.
//=========================
#define USAR_SERVIDOR_NATIVO 0

//=========================
// LCD
//=========================
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Pines I2C reales del XIAO ESP32S3 (D4=SDA=GPIO5, D5=SCL=GPIO6)
const int PIN_SDA = D4;
const int PIN_SCL = D5;

//=========================
// LEDs
//=========================
const int ledBlanco = D0;
const int ledUV = D1;

//=========================
// Sensores
//=========================
const int turbidezPin = A2;
const int conductividadPin = A3;

//=========================
// Variables de tiempo
//=========================
unsigned long inicioCiclo = 0;
unsigned long ultimaLectura = 0;
unsigned long ultimoFrame = 0;

const unsigned long INTERVALO_SENSOR = 1000;  // 1 segundo
const unsigned long INTERVALO_FRAME = 200;    // 5 FPS

// Ultimas lecturas (para reusar en el envio a Flask)
int ultimoTurbidez = 0;
int ultimaConductividad = 0;

#if USAR_SERVIDOR_NATIVO
void startCameraServer();
void setupLedFlash();
#endif

void setup() {

  Serial.begin(115200);
  delay(3000);

  pinMode(ledBlanco, OUTPUT);
  pinMode(ledUV, OUTPUT);
  pinMode(turbidezPin, INPUT);
  pinMode(conductividadPin, INPUT);

  digitalWrite(ledBlanco, LOW);
  digitalWrite(ledUV, LOW);

  Wire.begin(PIN_SDA, PIN_SCL);
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Sistema listo");
  delay(2000);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Inicia");
  lcd.setCursor(0, 1);
  lcd.print("el proceso...");
  delay(3000);

  lcd.clear();

  inicioCiclo = millis();

  Serial.println("================================");
  Serial.println("INICIO");
  Serial.printf("Modo: %s | Ciclo LED: %lu ms\n", MODO_PRUEBA ? "PRUEBA" : "REAL", TIEMPO_LED);
  Serial.println("================================");

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sccb_sda = SIOD_GPIO_NUM;
  config.pin_sccb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.frame_size = FRAMESIZE_UXGA;
  config.pixel_format = PIXFORMAT_JPEG;
  config.grab_mode = CAMERA_GRAB_WHEN_EMPTY;
  config.fb_location = CAMERA_FB_IN_PSRAM;
  config.jpeg_quality = 12;
  config.fb_count = 1;

  if (config.pixel_format == PIXFORMAT_JPEG) {
    if (psramFound()) {
      config.jpeg_quality = 10;
      config.fb_count = 2;
      config.grab_mode = CAMERA_GRAB_LATEST;
    } else {
      config.frame_size = FRAMESIZE_SVGA;
      config.fb_location = CAMERA_FB_IN_DRAM;
    }
  } else {
    config.frame_size = FRAMESIZE_240X240;
#if CONFIG_IDF_TARGET_ESP32S3
    config.fb_count = 2;
#endif
  }

#if defined(CAMERA_MODEL_ESP_EYE)
  pinMode(13, INPUT_PULLUP);
  pinMode(14, INPUT_PULLUP);
#endif

  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  sensor_t *s = esp_camera_sensor_get();
  if (s->id.PID == OV3660_PID) {
    s->set_vflip(s, 1);
    s->set_brightness(s, 1);
    s->set_saturation(s, -2);
  }
  if (config.pixel_format == PIXFORMAT_JPEG) {
    s->set_framesize(s, FRAMESIZE_QVGA);
  }

#if defined(CAMERA_MODEL_M5STACK_WIDE) || defined(CAMERA_MODEL_M5STACK_ESP32CAM)
  s->set_vflip(s, 1);
  s->set_hmirror(s, 1);
#endif

#if defined(CAMERA_MODEL_ESP32S3_EYE)
  s->set_vflip(s, 1);
#endif

#if USAR_SERVIDOR_NATIVO && defined(LED_GPIO_NUM)
  setupLedFlash();
#endif

  WiFi.begin(ssid, password);
  WiFi.setSleep(false);

  Serial.print("WiFi connecting");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");

#if USAR_SERVIDOR_NATIVO
  startCameraServer();
#endif

  Serial.print("Camera Ready! Use 'http://");
  Serial.print(WiFi.localIP());
  Serial.println("' to connect");
}

void enviarFrameFlask() {

  camera_fb_t *fb = esp_camera_fb_get();

  if (!fb) {
    Serial.println("Error capturando imagen");
    return;
  }

  HTTPClient http;
  http.begin(FLASK_URL_FRAME);
  http.addHeader("Content-Type", "image/jpeg");

  int codigo = http.POST(fb->buf, fb->len);

  if (codigo > 0) {
    Serial.printf("POST frame -> %d\n", codigo);
  } else {
    Serial.printf("Error HTTP frame: %s\n", http.errorToString(codigo).c_str());
  }

  http.end();
  esp_camera_fb_return(fb);
}

void enviarSensoresFlask(int turbidez, int conductividad) {

  if (WiFi.status() != WL_CONNECTED) return;

  HTTPClient http;
  http.begin(FLASK_URL_SENSORES);
  http.addHeader("Content-Type", "application/json");

  String json = "{\"turbidez\":" + String(turbidez) +
                ",\"conductividad\":" + String(conductividad) + "}";

  int codigo = http.POST(json);

  if (codigo > 0) {
    Serial.printf("POST sensores -> %d\n", codigo);
  } else {
    Serial.printf("Error HTTP sensores: %s\n", http.errorToString(codigo).c_str());
  }

  http.end();
}

void loop() {

  //=========================
  // Enviar imagen al servidor Flask
  //=========================
  if (millis() - ultimoFrame >= INTERVALO_FRAME) {
    ultimoFrame = millis();
    enviarFrameFlask();
  }

  //=========================
  // Tiempo del ciclo de LEDs
  //=========================
  unsigned long tiempo = millis() - inicioCiclo;

  if (tiempo < TIEMPO_LED) {
    digitalWrite(ledBlanco, HIGH);
    digitalWrite(ledUV, LOW);
  } else if (tiempo < (2 * TIEMPO_LED)) {
    digitalWrite(ledBlanco, LOW);
    digitalWrite(ledUV, HIGH);
  } else {
    inicioCiclo = millis();
  }

  //=========================
  // Lectura de sensores
  //=========================
  if (millis() - ultimaLectura >= INTERVALO_SENSOR) {
    ultimaLectura = millis();

    ultimoTurbidez = analogRead(turbidezPin);
    ultimaConductividad = analogRead(conductividadPin);

    Serial.printf("Turbidez: %d | Conductividad: %d\n", ultimoTurbidez, ultimaConductividad);

    lcd.setCursor(0, 0);
    lcd.print("Turb:");
    lcd.print(ultimoTurbidez);
    lcd.print("        ");

    lcd.setCursor(0, 1);
    lcd.print("Cond:");
    lcd.print(ultimaConductividad);
    lcd.print("        ");

    enviarSensoresFlask(ultimoTurbidez, ultimaConductividad);
  }
}
