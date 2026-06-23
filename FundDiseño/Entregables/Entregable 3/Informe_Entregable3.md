<p align="center">
  <img src="/Recursos/Imágenes/logo-upch.png" width="70%">
</p>

#  🔧 INFORME: ENTREGABLE 3

## 1. ESQUEMA ELECTRÓNICO 💾

## 1.1 DESCRIPCIÓN GENERAL

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

## 1.2 EXPLICACIÓN DE CONEXIONES:

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

## 2. DISEÑO MECÁNICO DEL PROTOTIPO

### 2.1 Descripción General

El módulo mecánico corresponde a la estructura física que integra y protege todos los componentes electrónicos del sistema Yaku-Ñawi. Su función principal es proporcionar soporte, estabilidad y protección a los sensores, microcontrolador, cámara, sistema de iluminación y fuente de alimentación, garantizando un correcto funcionamiento durante el análisis de muestras de agua.

El diseño fue desarrollado mediante la pagina de modelamiento 3D online "Onshape", considerando criterios de resistencia mecánica, facilidad de ensamblaje, portabilidad y acceso a los componentes para mantenimiento o futuras modificaciones.

### 2.2 Componentes Mecánicos Principales

#### ✅ Carcasa Principal

La carcasa constituye la estructura externa del dispositivo. Su diseño permite alojar de forma segura todos los módulos electrónicos, evitando daños por golpes, vibraciones o manipulación durante las pruebas experimentales.


<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/caja_3d.png" width="220px"><br><br>
      <sub>Imagen 10. Carcasa Principal </sub>
    </td>
  </tr>
</table>

Funciones:

* Protección de los componentes internos.
* Soporte estructural del sistema.
* Facilitar el transporte del prototipo.
* Mantener el ordenado cableado interno.



#### ✅ Soporte para lente

El lente fue instalada en un soporte que garantiza una orientación fija hacia la muestra analizada.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/soporte_lente.png" width="220px"><br><br>
      <sub>Imagen 11. Soporte para el lente </sub>
    </td>
  </tr>
</table>

Funciones:

* Mantener la distancia focal fija.
* Reducir errores por movimientos o vibraciones.
* Garantizar uniformidad en la captura de imágenes.

#### ✅ Placa para electronica

Se incorporó una placa para toda la electrónica(salvo la cámara, ya que es un sensor), además de  alojamientos para los LEDs UV-A y LEDs de luz blanca, como para la salida de cables para los sensores de turbidez y conductividad, ubicándolos estratégicamente para iluminar homogéneamente la muestra.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/placa_electrónica.png" width="220px"><br><br>
      <sub>Imagen 12. Placa para electrónica </sub>
    </td>
  </tr>
</table>

Funciones:

* Separar la electrónica de la muestra para evitar la exposición al agua.
* Aumentar altura para mayor visibilidad de los microplásticos.
* Minimizar sombras e interferencias lumínicas.

#### ✅ Placa para cámara

Se incorporó una placa exclusiva para la camara por dos motivos, separar la electronica de la camara, que la placa obstruya posible luz que pueda haber por parte de los orificios de la carcasa sin obstruir la salidas de los LEDs ni de los cables para los sensores.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/placa_cámara.png" width="220px"><br><br>
      <sub>Imagen 13. Placa para Cámara </sub>
    </td>
  </tr>
</table>
Funciones:

* Mencionadas en la descripcion anterior

#### ✅ Soporte para Powerbank

Se implementó un espacio destinado a la PowerBank , permitiendo una alimentación portátil y segura del equipo.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/soporte_powerbank.png" width="220px"><br><br>
      <sub>Imagen 14. Soporte para Powerbank </sub>
    </td>
  </tr>
</table>

Funciones:

* Facilitar la conexión eléctrica.
* Permitir el reemplazo de la fuente de energía.
* Mantener organizados los elementos de alimentación.

#### ✅ Puerta Inferior

Destinado a aislar la muestra de la luz, funciona a presión.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/puerta_inferior.png" width="220px"><br><br>
      <sub>Imagen 15. Puerta Inferior </sub>
    </td>
  </tr>
</table>

Funciones:

* Mencionadas en la descripcion anterior.

#### ✅ Puerta Superior

Misma Funcion de la puerta inferior, con la diferencia de tener una pantalla LCD destinada a mostrar resultados

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/puerta_superior.png" width="220px"><br><br>
      <sub>Imagen 16. Puerta Superior </sub>
    </td>
  </tr>
</table>

Funciones:

* Mencionadas en la descripcion anterior.


#### ✅ Cubierta para cámara

Con la funcion de evitar daños, tanto a la cámara como del procesador.

<table align="center" style="border: none; border-collapse: collapse;">
  <tr style="border: none;">
    <td align="center" style="border: none; padding: 15px; vertical-align: top;">
      <img src="/Recursos/Imágenes/cubierta_cámara.png" width="220px"><br><br>
      <sub>Imagen 17. Cubierta para cámara </sub>
    </td>
  </tr>
</table>

Funciones:

* Mencionadas en la descripcion anterior.
