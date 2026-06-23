# 📜 DESCRIPCIÓN Y APORTE DE NORMAS

<p align="center">
  <a href="https://www.une.org/encuentra-tu-norma/busca-tu-norma/norma/?c=N0073033" target="_blank">
    <img src="https://img.shields.io/badge/NORMA%201-Ver%20Enlace-baffc9?style=for-the-badge&logo=googlescholar&logoColor=white" style="margin-right: 5px;">
  </a>
  <a href="https://www.iso.org/obp/ui/en/#iso:std:iso:16094:-2:ed-1:v1:en" target="_blank">
    <img src="https://img.shields.io/badge/NORMA%202-Ver%20Enlace-e8aeff?style=for-the-badge&logo=googlescholar&logoColor=white" style="margin-right: 5px;">
  </a>
  <a href="https://www.iso.org/obp/ui/en/#iso:std:iso:7027:-1:ed-1:v1:en" target="_blank">
    <img src="https://img.shields.io/badge/NORMA%203-Ver%20Enlace-ffdac1?style=for-the-badge&logo=googlescholar&logoColor=white">
  </a>
</p>

### 📄 NORMA 1: UNE-EN ISO 7027-1 / ISO 7027-1 (Calidad del Agua - Determinación de la Turbidez)
-Resumen: Especifica los métodos estándar internacionales para determinar la turbidez del agua. Describe la metodología cuantitativa usando medidores ópticos de radiación (nefelómetros) para evaluar la concentración de partículas suspendidas basándose en cómo dispersan la luz.

-Aporte a Yaku-Ñawi: Es el fundamento matemático y físico directo de nuestro Sensor de Turbidez. Esta norma justifica técnicamente por qué usas un sensor óptico infrarrojo (LED emisor y fototransistor receptor) para leer el nivel de opacidad del agua antes de buscar microplásticos, permitiéndote calibrar el algoritmo en tu XIAO ESP32-S3 bajo rangos estandarizados de turbidez.

### 📄 NORMA 2: ISO 16094-2 (Plásticos - Evaluación de la Degradabilidad de Plásticos en Agua)
<p align="justify">
-Resumen: Establece los criterios y métodos estandarizados para evaluar la degradación física, pérdida de masa y fragmentación de materiales plásticos cuando están expuestos a ambientes acuáticos fluviales o marinos en condiciones controladas.
</p>
<p align="justify">
-Aporte a Yaku-Ñawi: Nos brinda el marco teórico para la clasificación del problema. Justifica la necesidad del prototipo, ya que los plásticos no desaparecen en el agua, sino que según esta norma se fragmentan continuamente hasta convertirse en microplásticos de tamaños milimétricos. Sustenta por qué el diseño del prototipo debe integrar una Cámara OV3660 con iluminación LED (UV-A y Blanco) para reconocer ópticamente esas partículas fragmentadas que la norma detalla.
</p>


### 📄 NORMA 3: ISO 7027-1 ()
<p align="justify">
-Resumen: Propone un método para concentrar y detectar nano/microplásticos en muestras de agua líquida aprovechando un efecto fototérmico guiado por láser que genera burbujas capilares para capturar las partículas suspendidas.
</p>
<p align="justify">
-Aporte a Yaku-Ñawi: Te sirve como sustento de antecedentes del problema. Demuestra que las tecnologías tradicionales de laboratorio (como la espectroscopía Raman) son sumamente complejas y costosas, lo cual le da un valor increíble al enfoque de Yaku-Ñawi, que busca un análisis in situ, portátil y de bajo costo utilizando mediciones directas (turbidez y conductividad/TDS) en campo.
</p>
