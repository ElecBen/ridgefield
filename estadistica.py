"""Estadistica descriptiva sin dependencias externas."""

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


def desviacion(datos):
    """La desviacion tipica de la muestra, con n-1 en el divisor."""
    if len(datos) < 2:
        raise ValueError("hacen falta al menos dos datos")
    centro = media(datos)
    cuadrados = sum((x - centro) ** 2 for x in datos)
    return math.sqrt(cuadrados / (len(datos) - 1))
