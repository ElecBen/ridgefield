"""Estadistica descriptiva sin dependencias externas."""

from __future__ import annotations

import math

__all__ = ["desviacion", "media", "mediana", "percentil"]


def media(datos: list[float]) -> float:
    """La media aritmetica de los datos."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    return sum(datos) / len(datos)


def mediana(datos: list[float]) -> float:
    """El valor central, o la media de los dos centrales si son pares."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    ordenados = sorted(datos)
    mitad = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[mitad]
    return (ordenados[mitad - 1] + ordenados[mitad]) / 2


def desviacion(datos: list[float]) -> float:
    """La desviacion tipica de la muestra, con n-1 en el divisor."""
    if len(datos) < 2:
        raise ValueError("hacen falta al menos dos datos")
    centro = media(datos)
    cuadrados = sum((x - centro) ** 2 for x in datos)
    return math.sqrt(cuadrados / (len(datos) - 1))


def percentil(datos, p):
    """El percentil `p` por interpolacion lineal entre vecinos."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    if not 0 <= p <= 100:
        raise ValueError("p debe estar entre 0 y 100")
    ordenados = sorted(datos)
    sitio = (len(ordenados) - 1) * p / 100
    bajo = int(sitio)
    if bajo == sitio:
        return ordenados[bajo]
    resto = sitio - bajo
    return ordenados[bajo] * (1 - resto) + ordenados[bajo + 1] * resto
