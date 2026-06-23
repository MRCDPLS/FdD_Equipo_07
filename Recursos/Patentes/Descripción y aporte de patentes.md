# 🫆 DESCRIPCIÓN Y APORTE DE PATENTES
<p align="center">
  <a href="https://worldwide.espacenet.com/patent/search?q=pn%3DWO2024066118A1" target="_blank">
    <img src="https://img.shields.io/badge/PATENTE%201-Ver%20Enlace-blue?style=for-the-badge&logo=target" style="margin-right: 5px;">
  </a>
  <a href="https://worldwide.espacenet.com/patent/search?q=pn%3DCN120334208A" target="_blank">
    <img src="https://img.shields.io/badge/PATENTE%202-Ver%20Enlace-blue?style=for-the-badge&logo=target" style="margin-right: 5px;">
  </a>
  <a href="https://worldwide.espacenet.com/patent/search?q=pn%3DUS2024125677A1" target="_blank">
    <img src="https://img.shields.io/badge/PATENTE%203-Ver%20Enlace-blue?style=for-the-badge&logo=target" style="margin-right: 5px;">
  </a>
  <a href="https://github.com/MRCDPLS/FdD_Equipo_07/blob/main/Recursos/Patentes/Patente%204-002302-2024DIN.pdf" target="_blank">
    <img src="https://img.shields.io/badge/PATENTE%204-Ver%20Enlace-blue?style=for-the-badge&logo=target">
  </a>
</p>
<p align="center">
  Accede al documento técnico.
</p>


## 📄 PATENTE 1 (W02024066118A1): Detección mediante Fusión de Imágenes RGB y Hiperespectrales
<p align="justify">
*Resumen:* Trata sobre un método de preprocesamiento, fusión de imágenes tradicionales (RGB) y espectros ópticos para detectar y segmentar de forma precisa partículas de microplásticos suspendidas en matrices sólidas o líquidas mediante IA.
</p>
<p align="justify">
*Aporte a tu proyecto:* Justifica directamente el uso de la Cámara OV3660 combinada con los LEDs (UV-A y Blanco). Valida que para identificar plásticos no basta con una foto común, sino que la estimulación de iluminación dual (color y luz ultravioleta para fluorescencia) permite a un microcontrolador captar de mejor manera las texturas y formas de los contaminantes.
</p>


## 📄 PATENTE 2 (CN_120334208_A): Espectroscopía Raman de Doble Haz mediante Deposición por Burbujas
<p align="justify">
*Resumen:* Propone un método para concentrar y detectar nano/microplásticos en muestras de agua líquida aprovechando un efecto fototérmico guiado por láser que genera burbujas capilares para capturar las partículas suspendidas.
</p>
<p align="justify">
*Aporte a tu proyecto:* Te sirve como sustento de antecedentes del problema. Demuestra que las tecnologías tradicionales de laboratorio (como la espectroscopía Raman) son sumamente complejas y costosas, lo cual le da un valor increíble al enfoque de Yaku-Ñawi, que busca un análisis in situ, portátil y de bajo costo utilizando mediciones directas (turbidez y conductividad/TDS) en campo.
</p>


## 📄 PATENTE 3 (US_2024/0125677_A1): Sistema electrónico de detección de tamaño de partícula chica
<p align="justify">
*Resumen:* Describe un dispositivo electrónico y un medio de escaneo que optimiza el tiempo de exposición de los sensores y cámaras para calcular con alta precisión el ratio de microplásticos pequeños (como PP y PET) directamente en muestras de agua fluviales.
</p>
<p align="justify">
*Aporte a tu proyecto:* Es el núcleo para el diseño algorítmico y matemático en tu ESP32-S3. Esta patente fundamenta la necesidad de controlar de forma digital (mediante los GPIOs) los tiempos de captura de la cámara y el procesamiento de señales analógicas simultáneas para evitar falsos positivos al medir plásticos pequeños.
</p>


## 📄 PATENTE 4 (002302-2024/DIN - Indecopi Perú): Equipo electrónico portátil para detección de microplásticos en agua
<p align="justify">
*Resumen:* Esta es una patente nacional de modelo de utilidad para un equipo portátil (con dimensiones específicas de ~11.5 cm y peso menor a 3 kg) diseñado para realizar análisis in situ de contaminación fluvial, guardando los datos en un sistema y enviándolos a través de conexiones inalámbricas. Cuenta con filtros ópticos y una pantalla LCD para interactuar.
</p>
<p align="justify">
*Aporte a tu proyecto:* Valida el empaquetado físico y arquitectónico de tu prototipo. Soporta técnicamente tu decisión de integrar una Pantalla LCD I2C para la interfaz del usuario y el uso de conectividad inalámbrica (aprovechando que el XIAO ESP32-S3 tiene Wi-Fi/Bluetooth de forma nativa) para transmitir los datos del sensor de turbidez y TDS.
</p>
