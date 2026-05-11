# ridgefield

![tests](https://github.com/ElecBen/ridgefield/actions/workflows/tests.yml/badge.svg)

Estadistica descriptiva sobre listas de numeros.

## Uso

```python
from estadistica import media, resumen

media([1, 2, 3])       # 2.0
resumen([1, 2, 3])     # {"n": 3, "media": 2.0, ...}
```

## Estructura

```
estadistica.py  modulo principal
tests/          tests con pytest
docs/           notas de diseno
```

## API

| funcion | que devuelve |
| --- | --- |
| `media(datos)` | la media aritmetica de los datos |
| `mediana(datos)` | el valor central, o la media de los dos centrales |
| `desviacion(datos)` | la desviacion tipica de la muestra |
| `percentil(datos, p)` | el percentil `p` interpolando entre los dos vecinos |
| `resumen(datos)` | un diccionario con las medidas de siempre |
| `atipicos(datos, veces)` | los valores que se salen del rango de Tukey |

## Medir

El banco de pruebas vive en `bench/` y se lanza como modulo, siempre desde la raiz del repo:

```
python -m bench.medir
```
