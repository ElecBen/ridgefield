# Notas de diseno

`desviacion()` divide por n-1, no por n: se asume que los datos son una
muestra y no la poblacion entera, que es el caso normal cuando se miden tiempos
o respuestas. Para la poblacion completa el numero sale un poco mas bajo.

`percentil()` interpola linealmente, que es una de las nueve
definiciones que hay. Con pocos datos las demas dan numeros distintos, asi que
comparar percentiles calculados con otra herramienta puede sorprender.

`atipicos()` devuelve los valores, no sus posiciones, y en el orden de
entrada. Marcar y no borrar es a proposito: quitar un dato de una serie es una
decision del analisis, no de la funcion que lo encuentra.
