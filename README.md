# Equipo 07 - Fundamentos de Diseño
### Carrera de Ingeniería Ambiental / Informática / Industrial  
**Universidad Peruana Cayetano Heredia**

---

## 🌍 Descripción del Equipo  
<p align="justify">
Somos el <strong>Equipo 07</strong> del curso <strong>Fundamentos de Diseño 2026</strong>, conformado por estudiantes de la carrera de Ingeniería Ambiental / Informática / Industrial.  
Nuestro objetivo es diseñar e implementar una solución tecnológica basada en metodologías de diseño que permita la detección y clasificación de microplásticos en ecosistemas marino, con el proposito de que las playas tengan el antiguo brillo de antes, y que los animales marinos esten bien. 
</p>

---

## 📌 Descripción del Proyecto
<p align="justify">
El equipo 07 desarrollará un disposito de detección automatizada de microplásticos mediante técnicas de procesamiento de imágenes, integrando hardware de bajo costo (como ESP32-CAM) y machine learning para su aplicación en entornos marinos con apoyo de la IA para diferenciarse de la competencia. La solución busca mejorar la identificación temprana de contaminantes y aportar a la mitigación de su impacto ambiental.
</p>

<p align="justify">
El objetivo principal de este proyecto es reducir reducir la presencia de microplásticos en entornos acuáticos, contribuyendo al cumplimiento de los ODS 6 (Agua limpia y saneamiento), 7 (Energía asequible y no contaminante) y 14 (Vida submarina).
</p>

---

## 🔍 Introducción

---

## ⚠️ Problemática 
### Problemática a Nivel Mundial
<p align="justify">
La crisis de los microplásticos está impulsada principalmente por polímeros de alta producción como el polipropileno (PP) y el polietileno tereftalato (PET). El polipropileno representa aproximadamente el 21 % de la producción total de plásticos no fibrosos, siendo ampliamente utilizado en envases, empaques y materiales industriales, lo que incrementa su liberación al ambiente tras su disposición final inadecuada (9). Por su parte, el PET constituye un material fundamental en la industria de bebidas y textiles sintéticos, donde domina la producción de fibras artificiales utilizadas globalmente (9,10).
</p>

#### Impactos y comportamiento:
* Persistencia diferencial: El PET tiende a degradarse más lentamente que otros polímeros como el polietileno, lo que prolonga su presencia en el entorno(10,11).
* Comportamiento en el agua: El PP posee una densidad aproximada de 0.94 g/mL, característica que le permite flotar y dispersarse ampliamente en la superficie marina. En contraste, el PET presenta mayor densidad, favoreciendo su sedimentación y acumulación en fondos acuáticos (10,11).
* Presencia en humanos: Diversas investigaciones han evidenciado la presencia de microplásticos en muestras biológicas humanas. Partículas de PP han sido detectadas en placenta y heces humanas, mientras que el PET constituye uno de los polímeros más frecuentemente identificados en sangre y muestras fecales, evidenciando su ingreso a la cadena alimentaria y posible impacto en la salud humana (10,12).

### Problemática a Nivel Local
<p align="justify">
En Lima y el Callao, el PP y el PET representan contaminantes prioritarios debido al elevado consumo de productos descartables y a deficiencias en la gestión integral de residuos sólidos. Se estima que cerca del 40 % de los residuos generados en el país no recibe una disposición adecuada, terminando en ríos, playas y ecosistemas marinos donde se fragmentan progresivamente en microplásticos (14).
</p>

#### Hallazgos específicos en Lima:
* Contaminación en playas: Estudios realizados en playas arenosas del litoral peruano han confirmado la presencia de microplásticos mediante análisis espectroscópicos, identificándose partículas de polipropileno asociadas a residuos marinos transportados por corrientes costeras y acumulación de basura oceánica (15).
* Riesgo en recursos pesqueros: Investigaciones recientes en especies comerciales capturadas en terminales pesqueros de Lima y Callao reportaron la presencia de microplásticos en el 100 % de algunas especies analizadas, evidenciando la transferencia de estas partículas dentro de la red trófica marina y su potencial riesgo para el consumo humano(14). El uso de PP en artes de pesca y la degradación de botellas de PET constituyen fuentes directas de contaminación en el ecosistema marino local (10,14).

## 💡 Presentación de la solución 
<p align="justify">
El presente proyecto propone el desarrollo de un <strong>sistema inteligente para la detección y clasificación de microplástico como el polipropileno (PP) y el polietileno tereftalato (PET)</strong> en cuerpos de agua, como lagunas y playas de Lima, donde la contaminación por residuos plásticos representa una amenaza creciente para los ecosistemas y la salud humana.
</p>

<p align="justify">
La solución se basa en la recolección de muestras de agua y sedimentos, seguida de su análisis mediante visión artificial y procesamiento de imágenes, lo que permite identificar y caracterizar partículas plásticas presentes en el entorno.
</p>

<p align="justify">
La arquitectura del sistema está compuesto por tres módulos principales:
</p>

### 🔹 Módulo 1: Recolección y filtrado  
- Captación de muestras de agua mediante un sistema manual o con bomba.
- Filtrado por mallas de diferentes tamaños.
- Separación de:
    - Macroplásticos (> 5 mm).
    - Microplásticos.  

### 🔹 Módulo 2: Registro y análisis 
- Integración de hardware (ej. ESP32-CAM).  
- Procesamiento con ImageJ: (17)
    - Identificación de partículas.
    - Medición de tamaño.

### 🔹 Módulo 3: Clasificación y registro inteligente  
- Uso de modelos de inteligencia artificial para clasificar polímeros:
    - PET (botellas).
    - PP (envases, tapas). 
- Registro de datos:
    - Cantidad de particulas.  
    - Tipo de plástico predominante.
    - Ubicación y tiempo de muestreo. 
- Visualización en una interfaz digital (app o dashboard).

<p align="justify">
Bajo el enfoque de ingeniería, el proyecto integra principalmente <strong>procesamiento de imágenes, machine learning, electrónica con sensores y microcontroladores</strong>. Esto permite transformar un proceso tradicionalmente manual en un sistema automatizado, escalable y replicable.
</p>

<p align="justify">
El valor innovador radica que <strong>automatiza la detección de microplásticos y macroplásticos, reduce costos frente a un análisis de laboratorio y que puede ser adaptada en distintas zonas del país</strong>.
</p>

---

## 🎯 Objetivos de Desarrollo Sostenible (ODS)
<p align="justify">
Nuestro proyecto se relaciona con los siguientes <strong>Objetivos de Desarrollo Sostenible (ODS)</strong>: 
</p>

- 🐠 **ODS 14 : VIDA SUBMARINA**  
  La contaminación por plásticos y microplásticos representa una amenaza importante para los ecosistemas marinos. Estas partículas pueden permanecer durante muchos años en el agua y afectar a la fauna marina. Se estima que entre 19 y 23 millones de toneladas de residuos plásticos ingresaron a los sistemas acuáticos en el 2016, y se prevé que esta cifra podría alcanzar hasta 53 millones de toneladas anuales para 2030. Esta problemática afecta directamente a la vida submarina, ya que los organismos marinos pueden ingerir microplásticos, lo que altera los ecosistemas y la biodiversidad.

---

- 💧 **ODS 6: AGUA LIMPIA Y SANEAMIENTO**  
  Los microplásticos también afectan la calidad del agua potable y los sistemas de tratamiento de aguas residuales. Estas partículas pueden ingresar a las plantas de tratamiento a través del lavado de ropa sintética y productos que contienen plástico. Aunque los sistemas de tratamiento pueden eliminar una parte de estos contaminantes, la gran cantidad de microplásticos sigue representando un desafío para garantizar agua segura y saneamiento adecuado.

---

- ⚡ **ODS 7: ENERGÍA ASEQUIBLE Y NO CONTAMINANTE**  
  Una de las formas de gestionar los residuos plásticos es la incineración para generar energía. Sin embargo, este proceso puede liberar gases de efecto invernadero que contribuyen al cambio climático. Estudios han estimado que las emisiones de gases de efecto invernadero provenientes de los plásticos podrían alcanzar 1.34 gigatoneladas por año para 2030, lo que evidencia la necesidad de soluciones sostenibles que reduzcan la contaminación y promuevan el uso responsable de los recursos energéticos. 
📊 Fuente: ScienceDirect(2021)

---

EJEMPLO  DE INICIATIVA RELACIONADA CON LA REDUCCIÓN DE MICRO PLÁSTICOS  

* El dispositivo creado por Zhang Dongqing y su equipo en 2021 ha transformado la detección de microplásticos en el océano al sustituir el lento proceso de recolección y análisis en laboratorio por un sistema de procesamiento directo que permite una separación eficiente y sencilla de las partículas contaminantes presentes en el agua de mar. Esta tecnología con forma de cilindro se instala verticalmente a través de un orificio roscado y utiliza un mecanismo avanzado de filtrado con presión positiva y negativa para aislar los microplásticos de manera inmediata a medida que el flujo de agua ingresa al sistema optimizando así las labores de monitoreo ambiental en tiempo real

* El creador Niu Xiaojun y su equipo crearon un dispositivo de recolección de micro plásticos con diferentes diámetros en agua de mar, incluye varios discos de recolección con ranuras verticales deslizantes para aumentar su eficiencia, patento su dispositivo en el año 2022.
El dispositivo de recolección incluye una caja de recolección, un componente de recolección, una caja de almacenamiento primaria, un cuerpo móvil subacuático y una fuente de alimentación para el dispositivo.

* Se presenta un dispositivo portátil diseñado para recolectar microplásticos mezclados con arena en playas.
El aparato está compuesto por un cabezal de succión que aspira los microplásticos, un conducto por donde estos son transportados y un bastidor principal que contiene una bolsa de recolección. El sistema incluye un cepillo electrostático que atrae los microplásticos mediante electricidad estática, permitiendo su separación eficiente de la arena. Finalmente, los microplásticos separados son transportados a través del conducto y almacenados en una bolsa de recolección, facilitando su manejo y eliminación.

* Una patente llamada "Dispositivo de recolección de muestras de microplásticos aplicado a costas marinas y playas" describe un sistema denominado Ocean Cleanup Autonomous System (OCAS), diseñado para la recolección, clasificación y transporte de residuos marinos mediante una red de embarcaciones autónomas interconectadas complementado con combustible. Asimismo, incorpora el uso de energías renovables (solar, eólica, undimotriz) y usa principios físicos de la electrostática y densidad.

---

## 📖 Referencias bibliográficas 

9. Geyer R, Jambeck JR, Law KL. Production, use, and fate of all plastics ever made. Sci Adv. 2017;3(7):e1700782. doi:10.1126/sciadv.1700782
10. Osman AI, Hosny M, Eltaweil AS, Omar S, Elgarahy AM, Farghali M, et al. Microplastic sources, formation, toxicity and remediation: a review. Environ Chem Lett. 2023;21:2129-2169. doi:10.1007/s10311-023-01593-3.
11. Rios Mendoza LM, Balcer M. Microplastics in freshwater environments: A review of quantification assessment. Trends Analyt Chem. 2019;113:402-408.
12. Hu B, Dai Y, Zhou H, Sun Y, Yu H, Dai Y, et al. Using artificial intelligence to rapidly identify microplastics pollution and predict microplastics environmental behaviors. J Hazard Mater. 2024;474:134865.
13. Tian X, Beén F, Bäuerlein PS. Quantum cascade laser imaging (LDIR) and machine learning for the identification of environmentally exposed microplastics and polymers. Environ Res. 2022;212:113569. doi:10.1016/j.envres.2022.113569
14. Ministerio del Ambiente (MINAM). Plásticos. Lima: Red Peruana Ciclo de Vida y Ecología Industrial (PELCAN); 2026.
15. Purca S, Henostroza A. Presencia de microplásticos en cuatro playas arenosas de Perú. Rev Peru Biol. 2017;24(1):101-106. doi:10.15381/rpb.v24i1.12724
16. Flores K, Seminario M, Canchari F, Alvariño L, Miñaya D, Castañeda L, et al. Contaminación por microplásticos en tres peces marinos del Perú. Rev Inv Vet Perú. 2026;37(1):e32888. doi:10.15381/rivep.v37i1.32888
17. Schneider CA, Rasband WS, Eliceiri KW. NIH Image to ImageJ: 25 years of image analysis. Nat Methods. 2012 Jul;9(7):671–5. doi:10.1038/nmeth.2089.

---

## 📸 Fotografía del Equipo  
<p align="center">
<img width="1408" height="768" alt="imagen_alumnos_IA" src="Recursos/Imágenes/foto grupal.jpeg" />
  <em>Figura 1. Fotografía del Equipo 07</em>
</p>

---

## 👥 Integrantes del Equipo  

| Foto | 👤 Nombre | 🎓 Rol | 💡 Intereses |
| :---: | :---: | :---: | :---: |
| <img src="/Recursos/Imágenes/rebeca.png" width="90"/> | **Rebeca Cerdan** | ❤️ Líder del equipo | 🎧 Melómana, 🤖 tecnología, 🎮 fan de Genshin Impact |
| <img src="/Recursos/Imágenes/Integrante2 .png" width="90"/> | **Siclali Fernandez** | 🚀 Product Manager | 🧠 Entender al usuario, 💡 soluciones innovadoras, 📢 comunicar el valor del proyecto  |
| <img src="/Recursos/Imágenes/integrante3.png" width="90"/> | **Marcelo Alarcon** | 🎨 Diseñador | 🧩 prototipos, ✨ creatividad, 🧱 modelado 3D, 🔍 investigador UX |
| <img src="/Recursos/Imágenes/integrante1.jpeg.jpeg" width="90"/> | **Mariluz Quispe** | 🌱 Encargada de Apoyo Ambiental | ♻️ sostenibilidad, 🌍 cuidado ambiental |
| <img src="/Recursos/Imágenes/bruno.png" width="90"/> | **Bruno Evangelista** | 💻 Programador y Modelador 3D | 📊 Programar una solución ecosostenible |

---

## 📌 Resumen final  
