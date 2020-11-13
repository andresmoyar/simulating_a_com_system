# simulating_a_com_system
El presente repositorio responde a la simulación de un sistema de comunicaciones tanto ideal como real, en la transmisión de imágenes a través de medios ruidosos. El proyecto cuenta con siete simulaciones que incluyen `codificación de fuente`, `codificación de canal`, `medios de transmisión` y `esquemas de modulación digital PAM/ASK`. Los componententes cubiertos en cada una de ellas contempla los siguientes componentes:
1. Componente: Codificación de fuente
2. Componente: codificación de fuente con canal binario simétrico
3. Componente: codificación de fuente con codificación de canal
4. Componente: codificación de fuente, codificación de canal y modulación banda base en un medio ideal
5. Componente: codificación de fuente, codificación de canal y modulación banda base en un medio con ruido
6. Componente: codificación de fuente, codificación de canal y modulación paso banda en un medio ideal
7. Componente: codificación de fuente, codificación de canal y modulación paso banda en un medio con ruido
8. Sistema de comunicaciones: codificación de fuente, codificación de canal, modulación y multiplexación en un medio con ruido`

![Screenshot]()

## Uso de las simulaciones
Para utilizar y valorar el funcionamiento de cada una de las simulaciones mostradas en la lista anterior inicie clonando este repositorio en algún directorio local de su computador utilizando la siguiente instrucción:

```
$ git clone https://github.com/JeaustinSirias/comunication_system_simulation_software.git
```
Una vez que cuente con el directorio de este proyecto, diríjase a la ruta del mismo a traves de su ventana de comandos. Este proyecto utiliza dependencias externas, de modo que si usted no está seguro de tener algunas de ellas, entonces puede digitar el siguiente comando para instalarlas:

```
$ make requirements
```
Cuando dichos cambios sean efectuados, puede entonces iniciar a probar cada una de las simulaciones del siguiente modo:
```
$ make run <identificador>
```
El `<identificador` hace referencia al número de simulación que usted desea ejecutar; por ejemplo, `sim1`, `sim2`, `sim3`, ..., `sim8`. Todas las simulaciones hacen uso de una imagen en formato BMP por defecto.

