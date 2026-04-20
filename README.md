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
El Equipo 07 desarrolla un dispositivo portátil de detección automatizada de microplásticos, enfocado en la identificación de polímeros como PP (polipropileno) y PET (polietileno tereftalato) en playas y humedales de Lima y Callao.

La solución integra técnicas de procesamiento digital de imágenes, visión computacional e inteligencia artificial, empleando hardware embebido basado en ESP32-CAM para su funcionamiento en entornos marino-costeros. El sistema captura imágenes de muestras ambientales y aplica modelos de IA para detectar y clasificar microplásticos directamente en campo, permitiendo diferenciar contaminantes de forma automática y eficiente.

El objetivo principal del proyecto es lograr la identificación temprana de microplásticos mediante un sistema autónomo capaz de procesar datos sin depender de infraestructura externa ni análisis de laboratorio especializados. Esto permite implementar un monitoreo ambiental continuo, oportuno y adaptado a condiciones reales, reduciendo tiempos, costos operativos y barreras tecnológicas existentes en los métodos tradicionales.

A través de esta propuesta tecnológica, el proyecto busca contribuir a la mitigación del impacto ambiental generado por la contaminación plástica en ecosistemas acuáticos, alineándose con los Objetivos de Desarrollo Sostenible, ODS 6 y ODS 14.
</p>

---

## 🔍 Introducción
<p align="justify">
En las últimas décadas, la producción y el uso masivo de plásticos han generado un incremento significativo de residuos sólidos en el ambiente, lo que ha ocasionado la acumulación de partículas plásticas en diversos ecosistemas a nivel mundial. Estas partículas, conocidas como microplásticos, se originan principalmente por la fragmentación de materiales plásticos de mayor tamaño y se han convertido en un contaminante emergente de gran preocupación ambiental y sanitaria (1,2).
</p>

<p align="justify">
Los microplásticos se definen como partículas plásticas con un tamaño menor a 5 mm y pueden encontrarse en una amplia variedad de entornos, incluyendo océanos, ríos, suelos y el aire. Debido a su pequeño tamaño y resistencia a la degradación, estas partículas permanecen en el ambiente durante largos periodos y pueden transportarse a través de diferentes medios naturales, lo que favorece su dispersión en ecosistemas acuáticos y terrestres (3,4). 
</p>

<p align="justify">
En el Perú, la gestión inadecuada de residuos sólidos y el manejo deficiente de los desechos costeros han favorecido la presencia de plásticos en ambientes marinos. Investigaciones científicas realizadas en la costa peruana han evidenciado la presencia de microplásticos en diferentes zonas, demostrando que estos contaminantes se distribuyen ampliamente y se generan a partir de la degradación continua de residuos plásticos en el ambiente (5).
</p>

<p align="justify">
Además de su presencia en el ambiente, los microplásticos también han sido detectados en organismos vivos, incluyendo especies marinas y seres humanos. Estudios científicos han demostrado que estas partículas pueden ingresar al cuerpo humano mediante la ingestión de alimentos contaminados o la inhalación de aire con partículas suspendidas, lo que ha generado preocupación sobre sus posibles efectos en la salud humana (6,7).
</p>

<p align="justify">
Diversas investigaciones han señalado que la exposición a microplásticos puede provocar efectos adversos en la salud, tales como inflamación, estrés oxidativo y alteraciones en tejidos y órganos. Asimismo, estos contaminantes representan una amenaza significativa para los ecosistemas, ya que afectan a organismos acuáticos y pueden alterar las cadenas alimentarias y la biodiversidad (2,8).
</p>

<p align="justify">
En este contexto, el presente proyecto tiene como objetivo determinar la presencia de microplásticos (MPs) en lagunas y playas de Lima, mediante la implementación de una metodología para su análisis e identificación, enfocándose en polímeros sintéticos de uso común como el polipropileno (PP) y el polietileno tereftalato (PET). Este tipo de estudios resulta fundamental para comprender la magnitud de la contaminación por microplásticos y contribuir al desarrollo de estrategias para la protección de los recursos hídricos y la salud ambiental (9).
</p>

<p align="justify">
Ante este escenario, resulta necesario implementar estrategias que permitan mitigar la acumulación de microplásticos en sedimentos y cuerpos de agua. En este sentido, la presente propuesta se enmarca en los Objetivos de Desarrollo Sostenible (ODS), específicamente en el ODS 6, orientado a la protección de la calidad del agua y la salud de los ecosistemas acuáticos, y en el ODS 14, enfocado en la reducción de la contaminación de origen terrestre que afecta la biodiversidad marina y la sostenibilidad de los océanos. De esta manera, se busca establecer una metodología de diagnóstico escalable y replicable para evaluar la presencia de polímeros sintéticos en cuerpos de agua lénticos y lóticos, contribuyendo a la generación de una base científica para la conservación del patrimonio hídrico del Perú (10).
</p>

---

## ⚠️ Problemática 
### Problemática a Nivel Mundial
<p align="justify">
La crisis de los microplásticos está impulsada principalmente por polímeros de alta producción como el polipropileno (PP) y el polietileno tereftalato (PET). El polipropileno representa aproximadamente el 21 % de la producción total de plásticos no fibrosos, siendo ampliamente utilizado en envases, empaques y materiales industriales, lo que incrementa su liberación al ambiente tras su disposición final inadecuada (11). Por su parte, el PET constituye un material fundamental en la industria de bebidas y textiles sintéticos, donde domina la producción de fibras artificiales utilizadas globalmente (11,12).
</p>

#### Impactos y comportamiento:
* Persistencia diferencial:
  <p align="justify">
  El PET tiende a degradarse más lentamente que otros polímeros como el polietileno, lo que prolonga su presencia en el entorno (10,11).
  </p>

* Comportamiento en el agua: 
  <p align="justify">
  El PP posee una densidad aproximada de 0.94 g/mL, característica que le permite flotar y dispersarse ampliamente en la superficie marina. En contraste, el PET presenta mayor densidad, favoreciendo su sedimentación y acumulación en fondos acuáticos (12,13).
  </p>

* Presencia en humanos: 
  <p align="justify">
  Diversas investigaciones han evidenciado la presencia de microplásticos en muestras biológicas humanas. Partículas de PP han sido detectadas en placenta y heces humanas, mientras que el PET constituye uno de los polímeros más frecuentemente identificados en sangre y muestras fecales, evidenciando su ingreso a la cadena alimentaria y posible impacto en la salud humana (12,13).
  </p>

### Problemática a Nivel Local
<p align="justify">
En Lima y el Callao, el PP y el PET representan contaminantes prioritarios debido al elevado consumo de productos descartables y a deficiencias en la gestión integral de residuos sólidos. Se estima que cerca del 40 % de los residuos generados en el país no recibe una disposición adecuada, terminando en ríos, playas y ecosistemas marinos donde se fragmentan progresivamente en microplásticos (16).
</p>

#### Hallazgos específicos en Lima:
* Contaminación en playas: 
  <p align="justify">
  Estudios realizados en playas arenosas del litoral peruano han confirmado la presencia de microplásticos mediante análisis espectroscópicos, identificándose partículas de polipropileno asociadas a residuos marinos transportados por corrientes costeras y acumulación de basura oceánica (17).
  </p>

* Riesgo en recursos pesqueros: 
  <p align="justify">
  Investigaciones recientes en especies comerciales capturadas en terminales pesqueros de Lima y Callao reportaron la presencia de microplásticos en el 100 % de algunas especies analizadas, evidenciando la transferencia de estas partículas dentro de la red trófica marina y su potencial riesgo para el consumo humano(16). El uso de PP en artes de pesca y la degradación de botellas de PET constituyen fuentes directas de contaminación en el ecosistema marino local (12,16,18).
  </p>

<p align="center">
  <img src="C:\Users\LENOVO\Desktop\FdD_Equipo_07\Recursos\Imágenes" width="500">
</p>
--- 

## 💡 Presentación de la solución 
<p align="justify">
El presente proyecto propone el desarrollo de un <strong>dispositivo inteligente portátil diseñado para detectar y clasificar microplásticos como el polipropileno (PP) y el polietileno tereftalato (PET)</strong> en cuerpos de agua, como humedales y playas de Lima y Callao, donde la contaminación por residuos plásticos representa una amenaza creciente para los ecosistemas y la salud humana.
</p>

<p align="justify">
La solución integra sensores ópticos, captura y procesamiento de imágenes y análisis automatizado usando modelos de IA, de muestras de agua y sedimentos. Este sistema incorpora algoritmos de machine learning y la inteligencia artificial actúa como núcleo del sistema, optimizando continuamente la detección a medida que procesa nuevas muestras. Todo ello se traduce en una herramienta portable y escalable, permitiendo realizar monitoreo ambiental directamente en campo sin necesidad de laboratorio especializado.
</p>

<p align="justify">
La arquitectura del sistema está compuesto por dos módulos principales:
</p>

### 🔹 Módulo 1: Registro y análisis 
- Integración de hardware (ej. ESP32-CAM).  
- Procesamiento con ImageJ: (19)
    - Identificación de partículas.
    - Medición de tamaño.

### 🔹 Módulo 2: Clasificación y registro inteligente  
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
  <p align="justify">
  La contaminación por plásticos y microplásticos representa una amenaza importante para los ecosistemas marinos. Estas partículas pueden permanecer durante muchos años en el agua y afectar a la fauna marina. Se estima que entre 19 y 23 millones de toneladas de residuos plásticos ingresaron a los sistemas acuáticos en el 2016, y se prevé que esta cifra podría alcanzar hasta 53 millones de toneladas anuales para 2030. Esta problemática afecta directamente a la vida submarina, ya que los organismos marinos pueden ingerir microplásticos, lo que altera los ecosistemas y la biodiversidad.
  </p>

- 💧 **ODS 6: AGUA LIMPIA Y SANEAMIENTO**  
  <p align="justify">
  Los microplásticos también afectan la calidad del agua potable y los sistemas de tratamiento de aguas residuales. Estas partículas pueden ingresar a las plantas de tratamiento a través del lavado de ropa sintética y productos que contienen plástico. Aunque los sistemas de tratamiento pueden eliminar una parte de estos contaminantes, la gran cantidad de microplásticos sigue representando un desafío para garantizar agua segura y saneamiento adecuado.
  </p>

---

## 📖 Referencias bibliográficas 
1.  Microplastics and human health. Wasser 3.0 [Internet]. 27 de julio de 2024 [citado 13 de abril de 2026]. Disponible en: https://wasserdreinull.de/en/blog/microplastics-and-human-health/?gad_source=1&gad_campaignid=22865333246&gbraid=0AAAAACT5X8xvzl5Wi7eAK0TEi-fi_-tUd&gclid=Cj0KCQjwqPLOBhCiARIsAKRMPZobmEIyfv4nfzCEhA3rrNn0mbGo0qEwoisLFwGIHgsIuUYYljt4h-caAhx1EALw_wcB 
2.  Snehamayee N, Somya S, Kumar SC, Niranjan M, Ranjan SB, Kumar MN. Microplastics and Human Health: A Comprehensive Review on Exposure Pathways, Toxicity, and Emerging Risks. Microplastics. marzo de 2026;5(1):8. doi:10.3390/microplastics5010008.
3. Lombardi G, Di Russo M, Zjalic D, Lanza T, Simmons M, Moscato U, et al. Microplastics inhalation and their effects on human health: a systematic review. Eur J Public Health. 25 de octubre de 2022;32(Suppl 3):ckac131.152. doi:10.1093/eurpub/ckac131.152 PubMed PMID: null; PubMed Central PMCID: PMC9835049. 
4. Luo Q, Tan H, Ye M, Jho EH, Wang P, Iqbal B, et al. Microplastics as an emerging threat to human health: An overview of potential health impacts. J Environ Manage. 1 de julio de 2025;387:125915. doi:10.1016/j.jenvman.2025.125915.
5. Micro- and mesoplastic pollution along the coast of Peru | Request PDF. ResearchGate. 23 de enero de 2026. doi:10.1007/s11356-023-27707-6.
6. Emenike EC, Okorie CJ, Ojeyemi T, Egbemhenghe A, Iwuozor KO, Saliu OD, et al. From oceans to dinner plates: The impact of microplastics on human health. Heliyon. 1 de octubre de 2023;9(10):e20440. doi:10.1016/j.heliyon.2023.e20440.
7. Thin ZS, Chew J, Ong TYY, Raja Ali RA, Gew LT. Impact of microplastics on the human gut microbiome: a systematic review of microbial composition, diversity, and metabolic disruptions. BMC Gastroenterol. 13 de agosto de 2025;25(1):583. doi:10.1186/s12876-025-04140-2 PubMed PMID: 40804621; PubMed Central PMCID: PMC12351775. 
8. Ririe AK, Fatema N, Dina TJ, Devi Kuchipudi J, Tamanna P, Libriansyah L, et al. Impact of Microplastic Exposure on Human Health: A Systematic Review of Mechanisms, Biomarkers, and Clinical Outcomes. Cureus. 28 de diciembre de 2025. doi:10.7759/cureus.100295.
9. Luque Fernández CR. Contaminación por microplásticos en playas arenosas de Islay, departamento de Arequipa [Internet]. 17 de enero de 2020 [citado 1 de abril de 2026]. Disponible en: https://repositorio.ucsm.edu.pe/handle/20.500.12920/9869. 
10. Gimiliani GT. Caracterização de microplásticos em amostras marinhas e estuarinas [tesis doctoral]. São Paulo: Instituto de Pesquisas Energéticas e Nucleares, Universidade de São Paulo; 2021. Disponible en: https://www.teses.usp.br/teses/disponiveis/85/85134/tde-22102021-104234/pt-br.php.
11. Geyer R, Jambeck JR, Law KL. Production, use, and fate of all plastics ever made. Sci Adv. 2017;3(7):e1700782. doi:10.1126/sciadv.1700782
12. Osman AI, Hosny M, Eltaweil AS, Omar S, Elgarahy AM, Farghali M, et al. Microplastic sources, formation, toxicity and remediation: a review. Environ Chem Lett. 2023;21:2129-2169. doi:10.1007/s10311-023-01593-3.
13. Rios Mendoza LM, Balcer M. Microplastics in freshwater environments: A review of quantification assessment. Trends Analyt Chem. 2019;113:402-408.
14. Hu B, Dai Y, Zhou H, Sun Y, Yu H, Dai Y, et al. Using artificial intelligence to rapidly identify microplastics pollution and predict microplastics environmental behaviors. J Hazard Mater. 2024;474:134865.
15. Tian X, Beén F, Bäuerlein PS. Quantum cascade laser imaging (LDIR) and machine learning for the identification of environmentally exposed microplastics and polymers. Environ Res. 2022;212:113569. doi:10.1016/j.envres.2022.113569
16. Ministerio del Ambiente (MINAM). Plásticos. Lima: Red Peruana Ciclo de Vida y Ecología Industrial (PELCAN); 2026.
17. Purca S, Henostroza A. Presencia de microplásticos en cuatro playas arenosas de Perú. Rev Peru Biol. 2017;24(1):101-106. doi:10.15381/rpb.v24i1.12724
18. Flores K, Seminario M, Canchari F, Alvariño L, Miñaya D, Castañeda L, et al. Contaminación por microplásticos en tres peces marinos del Perú. Rev Inv Vet Perú. 2026;37(1):e32888. doi:10.15381/rivep.v37i1.32888
19. Schneider CA, Rasband WS, Eliceiri KW. NIH Image to ImageJ: 25 years of image analysis. Nat Methods. 2012 Jul;9(7):671–5. doi:10.1038/nmeth.2089.

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
<p align="justify">
El proyecto del Equipo 07 propone un <strong>sistema inteligente para detectar y clasificar microplásticos (PP y PET)</strong> en las costas de Lima, utilizando <strong>hardware de bajo costo</strong> como la ESP32-CAM y modelos de inteligencia artificial para automatizar un proceso que usualmente es manual y costoso. La solución se divide en tres etapas que incluyen la recolección física de muestras, el análisis mediante visión artificial y el registro de datos en tiempo real, con el fin de <strong>proteger la biodiversidad marina y la salud humana</strong> frente a la alta contaminación de plásticos en el litoral peruano. Al alinearse con los <strong>Objetivos de Desarrollo Sostenible</strong> (Vida submarina, Agua limpia y Energía asequible), este dispositivo busca ser una herramienta escalable y eficiente para mitigar el impacto ambiental, inspirándose en tecnologías globales de filtrado y recolección electrostática para devolver la limpieza a los ecosistemas acuáticos.
</p>