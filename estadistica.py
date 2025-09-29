import math


def media(datos):
    """La media aritmetica de los datos."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    return sum(datos) / len(datos)


def mediana(datos):
    """El valor central, o la media de los dos centrales si son pares."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    ordenados = sorted(datos)
    mitad = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[mitad]
    return (ordenados[mitad - 1] + ordenados[mitad]) / 2
