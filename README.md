# SHA256 Custom Hash Function 
## Descripción
Este repositorio contiene una implementación en Python de una función personalizada basada en SHA256. La función toma como entrada un texto, una cadena de 256 bits en formato hexadecimal y un número de bits b. Generará un identificador concatenando el texto y la cadena proporcionados. Luego, se adjuntarán cadenas aleatorias x de 256 bits hasta lograr que SHA256(id||x) tenga sus primeros b bits a cero. La salida incluirá el identificador, la cadena x que produjo el hash requerido, el valor del hash y el número de intentos realizados para encontrar el valor apropiado de x.

## Instalación
```bash
pip install -r requirements.txt
``````

## Estructura del Repositorio
* custom_sha256.py: Contiene la implementación de la función personalizada SHA256.
* loop.py: Ejemplo de la funcion custom_sha256 para diferentes bits en formato json
* graphs.py: Para poder pintar los graficos con matplotlib
