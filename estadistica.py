import math


def media(datos):
    """La media aritmetica de los datos."""
    if not datos:
        raise ValueError("datos no puede estar vacio")
    return sum(datos) / len(datos)
