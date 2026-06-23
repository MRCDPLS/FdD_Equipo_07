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

## 1.1 EXPLICACIÓN DE CONEXIONES:

✅ _**Alimentación (PowerBank):**_
<p align="justify">
La PowerBank entrega +5V y GND a través de la bornera H5 (2 pines: pin 1 = +5V, pin 2 = GND). Incluye un switch SW2 para encender/apagar el sistema.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/5026548510714694858.jpg" width="220px"><br><br>
      <sub>Imagen 2. PowerBank.</sub>
    </td>
</table>

✅ _**XIAO ESP32-S3 (Microcontrolador):**_ 
<p align="justify">
Es el cerebro del circuito. Distribuye sus GPIOs así:</p>

<p align="justify">
• GPIO1 → LEDs.</p>
<p align="justify">
• GPIO2 → SDA de la pantalla LCD.</p>
<p align="justify">
• GPIO3 → Sensor de conductividad (TDS).</p>
<p align="justify">
• GPIO4 → Sensor de turbidez (SEN0189).</p>
<p align="justify">
• GPIO5 → SCL de la pantalla LCD.</p>
<p align="justify">
• GPIO6 → Cámara OV3660.</p>
<p align="justify">
• SCK, MISO, MOSI → Comunicación SPI con la cámara.</p>
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/xiao.jpg" width="280px"><br><br>
      <sub>Imagen 3. Microcontrolador XIAO ESP32-S3 Sense.</sub>
    </td>
  </tr>
</table>

✅ _**Cámara OV3660:**_ 
<p align="justify">
Se comunica con el ESP32-S3 mediante SPI (SCK, MISO, MOSI) y control por GPIO6. Se alimenta con VCC y GND.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/camera3660.png" width="280px"><br><br>
      <sub>Imagen 4. Cámara OV3660.</sub>
    </td>
  </tr>
</table>

✅ _**Sensor de Turbidez (TSW-20M):**_ 
<p align="justify">
• Bornera H2 (3 pines): pin 1 = GND, pin 2 = señal, pin 3 = 5V.</p>
<p align="justify">
• Se conecta al módulo SEN0189, el cual envía la señal analógica al GPIO4 del ESP32.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/turbity.jpg" width="320px"><br><br>
      <sub>Imagen 5. Sensor de Turbidez de agua (TSW-20M).</sub>
    </td>
  </tr>
</table>

✅ _**Sensor de Conductividad (TDS Meter V1.0):**_ 
<p align="justify">
• Bornera H4 (3 pines): pin 1 = GND, pin 2 = GPIO3, pin 3 = 5V.</p>
<p align="justify">
• El módulo TDS procesa la señal y la envía al GPIO3 del ESP32-S3.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/conductivity.jpg" width="320px"><br><br>
      <sub>Imagen 6. Sensor de Conductividad (TDS Meter V1.0).</sub>
    </td>
  </tr>
</table>

✅ _**Pantalla LCD:**_ 
<p align="justify">
• Se comunica por I2C: SDA → GPIO2, SCL → GPIO5.</p>
<p align="justify">
• Bornera H3 (4 pines): pin 1 = +5V, pin 2 = GND, pin 3 = GPIO2, pin 4 = GPIO5.</p>
<p align="justify">
• Incluye una resistencia R1 de 1KΩ en la línea de datos.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/pantallalcd.jpg" width="320px"><br><br>
      <sub>Imagen 7. Pantalla LCD I2C (16×2).</sub>
    </td>
  </tr>
</table>

✅ _**LEDs (UV-A y Blanco)**_ 
<p align="justify">
• Controlados desde GPIO1 del ESP32.</p>
<p align="justify">
• Tienen una resistencia limitadora R2 de 270Ω para proteger los LEDs.
</p>

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/led uva.jpg" width="250px"><br>
      <sub>Imagen 8. LED UV-A.</sub>
    </td>
    <td align="center" style="border: none; padding: 10px;">
      <img src="/Recursos/Imágenes/led white.jpg" width="250px"><br>
      <sub>Imagen 9. LED Blanco.</sub>
    </td>
  </tr>
</table>
# 🔧 INFORME: MÓDULO MECÁNICO GENERAL

## 2. DISEÑO MECÁNICO DEL PROTOTIPO

### 2.1 Descripción General

El módulo mecánico corresponde a la estructura física que integra y protege todos los componentes electrónicos del sistema Yaku-Ñawi. Su función principal es proporcionar soporte, estabilidad y protección a los sensores, microcontrolador, cámara, sistema de iluminación y fuente de alimentación, garantizando un correcto funcionamiento durante la adquisición y análisis de muestras de agua.

El diseño fue desarrollado mediante modelado 3D, considerando criterios de resistencia mecánica, facilidad de ensamblaje, portabilidad y acceso a los componentes para mantenimiento o futuras modificaciones.

### 2.2 Componentes Mecánicos Principales

#### ✅ Carcasa Principal

La carcasa constituye la estructura externa del dispositivo. Su diseño permite alojar de forma segura todos los módulos electrónicos, evitando daños por golpes, vibraciones o manipulación durante las pruebas experimentales.

Funciones:

* Protección de los componentes internos.
* Soporte estructural del sistema.
* Facilitar el transporte del prototipo.
* Mantener el ordenado cableado interno.

#### ✅ Compartimento para Sensores

Se diseñó una sección específica para la ubicación de los sensores de turbidez y conductividad, permitiendo una correcta exposición a las muestras de agua durante el proceso de medición.

Funciones:

* Mantener una posición fija de los sensores.
* Evitar desplazamientos durante las mediciones.
* Facilitar la inmersión y extracción de las sondas.

#### ✅ Soporte para Cámara

La cámara fue instalada en un soporte mecánico que garantiza una orientación constante hacia la muestra analizada.

Funciones:

* Mantener la distancia focal adecuada.
* Reducir errores por movimientos o vibraciones.
* Garantizar uniformidad en la captura de imágenes.

#### ✅ Sistema de Iluminación

Se incorporaron alojamientos para los LEDs UV-A y LEDs blancos, ubicándolos estratégicamente para iluminar homogéneamente la muestra.

Funciones:

* Mejorar la calidad de captura de imágenes.
* Resaltar características ópticas de los microplásticos.
* Minimizar sombras e interferencias lumínicas.

#### ✅ Compartimento de Alimentación

Se implementó un espacio destinado a la PowerBank y al sistema de encendido, permitiendo una alimentación portátil y segura del equipo.

Funciones:

* Facilitar la conexión eléctrica.
* Permitir el reemplazo de la fuente de energía.
* Mantener organizados los elementos de alimentación.

### 2.3 Materiales Utilizados

La estructura fue fabricada mediante impresión 3D utilizando material plástico de bajo peso y buena resistencia mecánica, adecuado para aplicaciones de prototipado y desarrollo tecnológico.

Las principales ventajas del material utilizado son:

* Bajo peso.
* Facilidad de fabricación.
* Resistencia suficiente para uso experimental.
* Posibilidad de modificaciones rápidas mediante rediseño e impresión.

### 2.4 Proceso de Diseño y Fabricación

El desarrollo del módulo mecánico comprendió las siguientes etapas:

1. Identificación de requerimientos del sistema.
2. Diseño conceptual de la estructura.
3. Modelado tridimensional mediante software CAD.
4. Verificación de dimensiones y compatibilidad con componentes electrónicos.
5. Fabricación mediante impresión 3D.
6. Ensamblaje y pruebas de funcionamiento.

### 2.5 Resultados del Diseño Mecánico

El módulo mecánico permitió integrar satisfactoriamente todos los subsistemas del proyecto, proporcionando una estructura estable, compacta y funcional. El diseño facilita el acceso a los componentes internos, mejora la organización del sistema y contribuye a la portabilidad del prototipo.

Asimismo, la disposición de la cámara, sensores y sistema de iluminación garantiza condiciones adecuadas para la adquisición de datos y detección de microplásticos en muestras de agua.

### 2.6 Conclusiones

El diseño mecánico desarrollado cumple con los requerimientos funcionales del proyecto, permitiendo la correcta integración de los componentes electrónicos y asegurando la estabilidad estructural del sistema. La fabricación mediante impresión 3D permitió obtener un prototipo ligero, resistente y adaptable a futuras mejoras del dispositivo.
