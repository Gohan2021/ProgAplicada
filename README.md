# PetVitals
## Introducción
El proyecto consiste en una aplicación que permita monitorear el estado de salud de mascotas (perros y gatos) en tiempo real, parametros como la presión arterial, ritmo cardiaco y respiratorio. Se proponen dos prototipos, el primero consiste en la implantación de un microchip tipo sensor que será colocado en la zona femural de la mascota, puesto que allí es un punto clave para la toma de los parametros fisiologicos pero que posee grandes dificultades para el diseño electrónico debido a que actualmente no existe tecnología del tamaño requerido para integrar un modulo bluethoot y sensor en un mismo microchip, pero que por temas de comodidad y efectivad seria el prototipo ideal, sin embargo se propone la alternativa de una "pulsera" la cual por temas de espacio posee la ventaja de integrar en ella el sistema de detección de los signos vitales, por lo que inicialmente so optaría por emplear este prototipo, y luego a traves de que la tecnología se miniaturice aún más emplear el prototipo de implantación de microchip.

El funcionamiento del sistema consiste en un sensor que permitirá leer los parámetros fisológicos tales como; La presión arterial, la frecuencia cardiaca y respiratoria, que su a vez va integrado con módulo bluethoot que permitirá la comunicación entre el sistema y la aplicacion. A continuación se detalla las variables fisiológicas a monitorear [Signos vitales de caninos y felinos](https://ateuves.es/parametros-fisiologicos-en-perros-y-gatos/#prettyPhoto/0/). 
![Procedimiento](https://stories.freepiklabs.com/storage/16179/Animal-Shelter-01.svg)

### Variables fisiológicas
* #### Presión Arterial: 
  Es la fuerza con la que la sangre empuja a las paredes arteriales y existen diferentes tipos de presiones:
  
  1. Presión arterial diastólica: Esta se refiere a una presión más baja entre latidos es decir, cuando el corazón se encuentra en reposo. (T. Mahecha, 2021)
  2. Presión arterial sistólica: Contraria a diastólica se refiere a una presión más alta entre latidos. (T. Mahecha, 2021)
* #### Frecuencia cardiaca:
  Consiste en el número de contracciónes del corazón por minuto, en felinos el promedio es de 140 a 220 latidos por minuto y en caninos el       promedio es de 60 a  180 latidos por minuto (T. Mahecha, 2021)
* #### Frecuencia respiratoria: 
  Se define como el número de veces que se respirta en un periodo, en felinos es de 20 a 40 respiraciones por minuto y en caninos el promedio es de 10 a 30 respiraciones por minuto (T. Mahecha, 2021)
  
## Estado del arte
+ En China se desarrolló un sistema para mascotas el cual es un alimentador inteligente
que en pocas palabras es un sistema que le permite al dueño programar la comida del animal por tiempo. (Own, et. al, 2013)

+ El conocido localizador GPS que permite saber en riempo real la ubicación de la mascota que consiste de una antena GPS y un hardware que primte ubicación en cualquier parte del mundo.(Tractive, 2022)

+ Microchip; Consiste en una implantación de un microchip a la mascota con el fin de que posea un número único que puede ser leido cuando se encuentre perdida la mascota, sin embargo no cuenta con mucha cobertura y solo puede ser detectado con equipos situados en veterinarios o citios especializados. (Tractive, 2022)

## Ventajas de VetVitals
  VetVitals es efectivo para detectar anomalías en los signos vitales de tu mascota, ya que teniendo información de las variables fisiologicas como la presión arterial que puede indicar si la mascota está hipertenso o hipotenso, lo que puede darnos un aviso de que la mascota puede presentar deshidratación, o un fallo en algún organo, al igual que otro tipo de patologías a partir de la información de los signos vitales. Lo que nos permite concluir que los signos vitales son fundamentales para una buena salud de las mascotas y que permite a los veterinarios tener una información más detallada de como se encuentran las mascotas para un previo análisis. (T. Mahecha, 2021)

## Referencias
* Tractive(octubre 2022)Resumen de las diferencias entre un localizador para perros y un microchip, https://tractive.com/blog/es/seguridad/diferencias-microchip-para-perros-y-tractive-gps
* Tania Lorena Mahecha Montero(abril 2021) Análisis de los parámetros fisiológicos de monitoreo en pacientes caninos y
felinos internados en la uci en la clínica veterinaria punto vet, MedellínColombia
https://repository.ucc.edu.co/server/api/core/bitstreams/e7869a5f-6dd8-4e16-8e8f-8550f3d42da5/content
