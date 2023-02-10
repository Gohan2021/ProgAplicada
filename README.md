# Aplicacion que muestra el estado de salud de un animal
## Introducción
El proyecto consiste en una aplicación que permita monitorear el estado de salud de mascotas (perros y gatos) en tiempo real, parametros como la presión arterial, ritmo cardiaco y respiratorio. Se proponen dos prototipos, el primero consiste en la implantación de un microchip tipo sensor que será colocado en la zona femural de la mascota, puesto que allí es un punto clave para la toma de los parametros fisiologicos pero que posee grandes dificultades para el diseño electrónico debido a que actualmente no existe tecnología del tamaño requerido para integrar un modulo bluethoot y sensor en un mismo microchip, pero que por temas de comodidad y efectivad seria el prototipo ideal, sin embargo se propone la alternativa de una "pulsera" la cual por temas de espacio posee la ventaja de integrar en ella el sistema de detección de los signos vitales, por lo que inicialmente so optaría por emplear este prototipo, y luego a traves de que la tecnología se miniaturice aún más emplear el prototipo de implantación de microchip.

El funcionamiento del sistema consiste en un sensor que permitirá leer los parámetros fisológicos tales como; La presión arterial, la frecuencia cardiaca y respiratoria, que su a vez va integrado con módulo bluethoot que permitirá la comunicación entre el sistema y la aplicacion. A continuación se detalla las variables fisiológicas a monitorear 

### Variables fisiológicas
* ####Presión Arterial: Es la fuerza con la que la sangre empuja a las paredes arteriales y existen diferentes tipos de presiones
  1. Presión arterial diastólica: Esta se refiere a una presión más baja entre latidos es decir, cuando el corazón se encuentra en reposo.
  2. Presión arterial sistólica: Contraria a diastólica se refiere a una presión más alta entre latidos.
* ####Frecuencia cardiaca: Consiste en el número de contracciónes del corazón por minuto, en felinos el promedio es de 140 a 220 latidos por minuto y en caninos el       promedio es de 60 a 180 latidos por minuto
* ####Frecuencia respiratoria: Se define como el número de veces que se respirta en un periodo, en felinos es de 20 a 40 respiraciones por minuto y en caninos el promedio es de 10 a 30 respiraciones por minuto


## Estado del arte


![Procedimiento](https://bogota.gov.co/sites/default/files/inline-images/whatsapp-image-2021-06-22-at-16.50.42_0.jpeg)

## Indice
* Primera semana 
  1. Virtual
    - Chat gtp
    - Replit
    - Python
  2. Computador
  3. Cuaderno 
* Segunda semana
