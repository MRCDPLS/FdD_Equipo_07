# Taller nro 14

## Actividad 1


---

### Imagen del bloque de MIT App Inventor
A continuación se presenta el bloque del MIT App Inventor

![https://drive.google.com/file/d/1D5xYZtxJiR00PYCBLBq80FJNMhT6WZPw/view?usp=drive_link](https://drive.google.com/file/d/1D5xYZtxJiR00PYCBLBq80FJNMhT6WZPw/view?usp=drive_link)

---
### Imagen del Designer de MIT App Inventor
A continuación se presenta el Designer del MIT App Inventor

![Design Actividad 2](https://drive.google.com/file/d/1QXypt_W8udMlN-QIv3HKQZ5a85_nzcKo/view?usp=drive_link)

---

### Bloque de Código en ARDUINO IDE
Aquí se muestra el codigo usado en ARDUINO IDE para el correcto funcionamiento:

```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include "BluetoothSerial.h"
BluetoothSerial SerialBT;
LiquidCrystal_I2C lcd(0x27, 16, 2);
void setup() {
  lcd.init();
  lcd.backlight();

  SerialBT.begin("ESP32_LCD");

  lcd.setCursor(0, 0);
  lcd.print("Esperando...");
}
void loop() {
  if (SerialBT.available()) {

    String mensaje = SerialBT.readStringUntil('\n');
    mensaje.trim();

    lcd.clear();

    if (mensaje.length() <= 16) {
      // Cabe en una sola fila
      lcd.setCursor(0, 0);
      lcd.print(mensaje);
    } else {
      // Se divide en dos filas
      lcd.setCursor(0, 0);
      lcd.print(mensaje.substring(0, 16));
      lcd.setCursor(0, 1);
      lcd.print(mensaje.substring(16, 32));
    }
  }
}
```

---

### Enlace a Recurso de Video
El enlace a continuacion muestra como funciona:

Enlace al video: [Ver Video](https://drive.google.com/file/d/1oEB_WucguHfDKxK_4054fNlgEVF8Y4Jw/view?usp=drive_link)

### Como funciona
Esta práctica se enfoca en el control dinámico de actuadores utilizando tecnologías de red inalámbricas como Bluetooth o WiFi. El propósito fundamental es diseñar una interfaz gráfica en MIT App Inventor que disponga de una barra deslizante (denominada slider). Al mover este control en la pantalla del smartphone, se envían datos numéricos en tiempo real hacia el ESP32, el cual decodifica la señal para modificar con precisión el ángulo de giro de un servomotor acoplado al sistema.

En el apartado de hardware, la complejidad del cableado se reduce en comparación con la primera actividad, ya que se emplean menos componentes externos. Los materiales necesarios se limitan al módulo ESP32 DevKit V1 como cerebro del proyecto, un servomotor específico modelo 35G-CM con capacidad de rotación de hasta 270°, el cable micro-USB para la transferencia del código junto a la alimentación eléctrica, y el dispositivo Android que actúa como el panel de control interactivo.
## Actividad 2

---

### Imagen del bloque de MIT App Inventor
A continuación se presenta el bloque del MIT App Inventor

![Bloque Actividad 2](https://drive.google.com/file/d/1k5u4m1aDOfD-LFQjilzLEEmkRXQ-nm-8/view?usp=drive_link)

---
### Imagen del Designer de MIT App Inventor
A continuación se presenta el Designer del MIT App Inventor

![Design Actividad 2](https://drive.google.com/file/d/1g2GzaLHDTw6mZWex8EHxU-rcTl4cUilY/view?usp=drive_link)

---

### Bloque de Código en ARDUINO IDE
Aquí se muestra el codigo usado en ARDUINO IDE para el correcto funcionamiento:

```cpp
#include <WiFi.h>
#include <WebServer.h>

// Configuración del pin y PWM nativo para el servo
const int pinServo = 1; // Pin D0 en la XIAO ESP32-S3
const int frecuencia = 50;
const int resolucion = 12;

// Nombre y contraseña de la red Wi-Fi que creará la XIAO
const char* ssid = "XIAO_Servo_Net";
const char* password = "123456789_XIAO";

// Creamos el servidor web en el puerto 80
WebServer server(80);

void moverServo(int angulo) {
  int duty = map(angulo, 0, 270, 102, 491);
  ledcWrite(pinServo, duty);
}

// Función que se ejecuta cuando el celular manda el ángulo
void manejarRutaServo() {
  if (server.hasArg("angulo")) {
    String valor = server.arg("angulo");
    int angulo = valor.toInt();
    
    if (angulo >= 0 && angulo <= 270) {
      moverServo(angulo);
      Serial.print("Ángulo recibido por Wi-Fi: ");
      Serial.println(angulo);
    }
    server.send(200, "text/plain", "OK");
  } else {
    server.send(400, "text/plain", "Falta el parámetro 'angulo'");
  }
}

void setup() {
  Serial.begin(115200);
  
  // Configurar PWM del servo
  ledcAttach(pinServo, frecuencia, resolucion);
  moverServo(0); // Iniciar en 0 grados

  // Configurar la XIAO en modo Access Point
  Serial.println("Configurando Access Point...");
  WiFi.softAP(ssid, password);
  
  IPAddress IP = WiFi.softAPIP();
  Serial.print("Red Wi-Fi lista. IP del servidor: ");
  Serial.println(IP); // Por defecto será 192.168.4.1

  // Definir la ruta web para el control del servo
  server.on("/setServo", manejarRutaServo);
  
  // Iniciar el servidor
  server.begin();
  Serial.println("Servidor HTTP iniciado.");
}

void loop() {
  server.handleClient(); // Mantener el servidor atento a peticiones
}
```

---

### Enlace a Recurso de Video
El enlace a continuacion muestra como funciona:

Enlace al video: [Ver Video](https://drive.google.com/file/d/1lbO74vRa-t-MmN_bKW8oT_3HK0gYHMYx/view?usp=sharing)

### Como funciona
El objetivo principal de este proyecto es diseñar e implementar un sistema de comunicación inalámbrica de corto alcance. Consiste en desarrollar una aplicación móvil personalizada mediante la plataforma MIT App Inventor que se conecte vía Bluetooth a un módulo ESP32 DevKit V1. La meta final es redactar un mensaje de texto desde un smartphone Android y transmitirlo de forma inalámbrica para que el microcontrolador lo procese y lo muestre en una pantalla LCD de 2x16 caracteres.

Para llevar a cabo este montaje electrónico, se requiere un conjunto específico de componentes que aseguren el correcto funcionamiento del hardware. Además del módulo ESP32 y el teléfono inteligente, la lista de materiales incluye una pantalla LCD 2x16, una resistencia de 220 Ω para proteger la retroiluminación y un potenciómetro de 10 kΩ para regular el contraste de las letras en el panel. Todo el sistema se energiza y se programa utilizando un cable de datos micro-USB conectado al módulo principal.
