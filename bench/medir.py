"""Mide percentil() sobre una muestra grande.

Se ejecuta desde la raiz del repo para que `estadistica` este en la ruta:

    python -m bench.medir
"""
import random
import time

from estadistica import percentil


def main():
    datos = [random.random() for _ in range(2000000)]
    arranque = time.perf_counter()
    p95 = percentil(datos, 95)
    print("p95=%.4f en %.3f s" % (p95, time.perf_counter() - arranque))


if __name__ == "__main__":
    main()
