# 💼 TECNOLOGÍA EXISTENTE EN EL ÁMBITO COMERCIAL

<table width="100%">
  <!-- PRODUCTO 1: HORIBA -->
  <tr bgcolor="#2c3e50">
    <th colspan="2" align="center" style="color: white; padding: 10px;">
      <h3>1. LabRAM HR Evolution Raman Microscope — HORIBA Scientific</h3>
    </th>
  </tr>
  <tr>
    <td width="30%" align="center" bgcolor="#f8f9fa">
      <br>
      <!-- Asegúrate de subir la imagen a tu repositorio y referenciar la ruta correcta aquí -->
      <img src="RUTA_DE_TU_IMAGEN_1/image_d49cee.png" width="85%" alt="Microscopio Raman LabRAM HR Evolution"><br>
      <sub><b>Figura 1:</b> Microscopio Raman LabRAM HR Evolution para análisis ambiental.</sub>
    </td>
    <td>
      <table width="100%">
        <tr bgcolor="#f2f4f4"><th>Características Técnicas</th><th>Detalles del Dispositivo</th></tr>
        <tr><td><b>Técnica Analítica:</b></td><td>Espectroscopía Raman (Dispersión de luz láser)</td></tr>
        <tr><td><b>Fuente de Excitación:</b></td><td>Láser de múltiples longitudes de onda (405 nm, 532 nm, 633 nm y 785 nm)</td></tr>
        <tr><td><b>Automatización:</b></td><td>Mapeo químico automático y escaneo automatizado en 2D y 3D</td></tr>
        <tr><td><b>Software de Control:</b></td><td>LabSpec Raman Software (Clasificación con bibliotecas espectrales)</td></tr>
        <tr><td><b>Operación Estándar:</b></td><td>Laboratorio científico especializado de alto costo</td></tr>
      </table>
    </td>
  </tr>
  <tr>
    <td bgcolor="#eaecee"><b>Aporte y Justificación a Yaku-Ñawi:</b></td>
    <td bgcolor="#f4f6f7" align="justify">
      <ul>
        <li><b>Sustento del problema (Costo y Portabilidad):</b> Este equipo comercial demuestra que las alternativas actuales requieren laboratorios especializados y operativas complejas. Esto justifica la propuesta de valor de Yaku-Ñawi como una alternativa <b>portátil, directa y de bajo costo</b> para mediciones <i>in situ</i>.</li>
        <li><b>Validación de Fluorescencia:</b> El sistema de HORIBA usa láseres específicos para mitigar la interferencia por fluorescencia de ciertas muestras ambientales. Esto valida directamente nuestra integración de <b>LEDs de iluminación dual (UV-A y Blanco)</b> en Yaku-Ñawi para excitar los materiales de manera controlada y captar mejor las características ópticas mediante la cámara OV3660.</li>
      </ul>
    </td>
  </tr>

  <!-- ESPACIO DE SEPARACIÓN -->
  <tr><td colspan="2" style="padding: 10px; border: none;"></td></tr>

  <!-- PRODUCTO 2: BRUKER -->
  <tr bgcolor="#34495e">
    <th colspan="2" align="center" style="color: white; padding: 10px;">
      <h3>2. LUMOS II FT-IR Microscope — Bruker Corporation</h3>
    </th>
  </tr>
  <tr>
    <td width="30%" align="center" bgcolor="#f8f9fa">
      <br>
      <!-- Asegúrate de subir la imagen a tu repositorio y referenciar la ruta correcta aquí -->
      <img src="RUTA_DE_TU_IMAGEN_2/image_d49dcd.png" width="85%" alt="Sistema FT-IR LUMOS II"><br>
      <sub><b>Figura 2:</b> Sistema FT-IR LUMOS II para análisis de microplásticos.</sub>
    </td>
    <td>
      <table width="100%">
        <tr bgcolor="#f2f4f4"><th>Características Técnicas</th><th>Detalles del Dispositivo</th></tr>
        <tr><td><b>Técnica Analítica:</b></td><td>Micro-FTIR (Fourier Transform Infrared Spectroscopy)</td></tr>
        <tr><td><b>Fuente de Excitación:</b></td><td>Radiación infrarroja (IR) de absorción molecular</td></tr>
        <tr><td><b>Modos de Análisis:</b></td><td>ATR, transmisión y reflexión (Detectores FPA)</td></tr>
        <tr><td><b>Software de Control:</b></td><td>OPUS / Particle & Microplastics Analysis</td></tr>
        <tr><td><b>Rango de Detección:</b></td><td>Desde micrómetros hasta milímetros (Muestras de agua y sedimentos)</td></tr>
      </table>
    </td>
  </tr>
  <tr>
    <td bgcolor="#eaecee"><b>Aporte y Justificación a Yaku-Ñawi:</b></td>
    <td bgcolor="#f4f6f7" align="justify">
      <ul>
        <li><b>Clasificación de Polímeros:</b> El software de Bruker clasifica automáticamente plásticos como Polietileno (PE), PET y Poliestireno (PS). Esto establece el benchmark del problema comercial y justifica que el algoritmo cargado en nuestro microcontrolador <b>XIAO ESP32-S3</b> apunte a clasificar el mismo tipo de polímeros comunes en matrices de agua fluviales.</li>
        <li><b>Filosofía de Reconocimiento Automático:</b> El LUMOS II basa su eficiencia en la automatización del mapeo de partículas para eliminar el descarte manual lento. Yaku-Ñawi replica conceptualmente esta necesidad mediante visión artificial embebida, procesando la turbidez del agua y capturando imágenes para automatizar la alerta de contaminantes de forma rápida sin analistas de laboratorio.</li>
      </ul>
    </td>
  </tr>
</table>
