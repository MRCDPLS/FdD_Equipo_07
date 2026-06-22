<p align="center">
  <img src="/Recursos/Imágenes/logo-upch.png" width="70%">
</p>

#  🔧 INFORME: ENTREGABLE 3

## 1. ESQUEMA ELECTRÓNICO 💾
<p align="justify">
En esta sección, presentamos el circuito esquemático de nuestro proyecto utilizando la herramienta EasyEDA para el diseño, simulación y fabricación de circuitos electrónicos y placas de circuito impreso (PCB). Se trata de una representación gráfica de un circuito eléctrico que emplea símbolos estandarizados para ilustrar tanto los componentes como las conexiones entre ellos. Este tipo de diagrama es ampliamente utilizado en electrónica para describir y visualizar la disposición de los elementos de un sistema.
</p>
<p align="justify">
En nuestro caso, el esquemático muestra cómo se integran todos los componentes del proyecto en un único circuito, detallando aspectos como la asignación de pines, la dirección de las señales y las conexiones entre cada elemento. A continuación, presentamos el diagrama para su visualización.
</p>

<p align="center">
  <img src="/Recursos/Imágenes/Esquemático Final de Yaku-Ñawi.png" width="70%">
</p>

<p align="center">Imagen 1. Circuito electrónico del proyecto general en EasyEDA. </p>

## EXPLICACIÓN DE CONEXIONES:

_**- Alimentación (PowerBank):**_
<p align="justify">
La PowerBank entrega +5V y GND a través de la bornera H5 (2 pines: pin 1 = +5V, pin 2 = GND). Incluye un switch SW2 para encender/apagar el sistema.
</p>

_**- XIAO ESP32-S3 (Microcontrolador):**_ 
<p align="justify">
Es el cerebro del circuito. Distribuye sus GPIOs así:

• GPIO1 → LEDs
• GPIO2 → SDA de la pantalla LCD
• GPIO3 → Sensor de conductividad (TDS)
• GPIO4 → Sensor de turbidez (SEN0189)
• GPIO5 → SCL de la pantalla LCD
• GPIO6 → Cámara OV3660
• SCK, MISO, MOSI → Comunicación SPI con la cámara
</p>

_**- Cámara OV3660**_ 
<p align="justify">
Se comunica con el ESP32-S3 mediante SPI (SCK, MISO, MOSI) y control por GPIO6. Se alimenta con VCC y GND.
</p>

_**- Sensor de Turbidez (SEN0189)**_ 
<p align="justify">
• Bornera H2 (3 pines): pin 1 = GND, pin 2 = señal, pin 3 = 5V
• Se conecta al módulo SEN0189, el cual envía la señal analógica al GPIO4 del ESP32
</p>

_**- Sensor de Conductividad (TDS Meter V1.0)**_ 
<p align="justify">
• Bornera H4 (3 pines): pin 1 = GND, pin 2 = GPIO3, pin 3 = 5V
• El módulo TDS procesa la señal y la envía al GPIO3 del ESP32-S3
</p>

_**- Pantalla LCD**_ 
<p align="justify">
• Se comunica por I2C: SDA → GPIO2, SCL → GPIO5
• Bornera H3 (4 pines): pin 1 = +5V, pin 2 = GND, pin 3 = GPIO2, pin 4 = GPIO5
• Incluye una resistencia R1 de 1KΩ en la línea de datos
</p>

_**- LEDs (UV-A y Blanco)**_ 
<p align="justify">
• Controlados desde GPIO1 del ESP32
• Tienen una resistencia limitadora R2 de 270Ω para proteger los LEDs
</p>
