import pytest

from estadistica import (atipicos, desviacion, media, mediana, percentil,
                         resumen)


def test_media():
    assert media([1, 2, 3]) == 2


def test_media_con_decimales():
    assert round(media([1, 2]), 3) == 1.5


def test_media_de_nada():
    with pytest.raises(ValueError):
        media([])


def test_mediana_impar():
    assert mediana([3, 1, 2]) == 2


def test_mediana_par():
    assert mediana([1, 2, 3, 4]) == 2.5


def test_mediana_de_nada():
    with pytest.raises(ValueError):
        mediana([])


def test_desviacion():
    assert round(desviacion([1, 2, 3, 4]), 3) == 1.291


def test_desviacion_de_datos_iguales_es_cero():
    assert desviacion([5, 5, 5]) == 0


def test_desviacion_de_un_solo_dato():
    with pytest.raises(ValueError):
        desviacion([1])


def test_percentil_del_medio_es_la_mediana():
    assert percentil([1, 2, 3, 4], 50) == mediana([1, 2, 3, 4])


def test_percentil_en_las_puntas():
    assert percentil([1, 2, 3], 0) == 1
    assert percentil([1, 2, 3], 100) == 3


def test_percentil_interpola():
    assert round(percentil([1, 2, 3, 4], 25), 3) == 1.75


def test_percentil_fuera_de_rango():
    with pytest.raises(ValueError):
        percentil([1, 2], 150)


def test_resumen_trae_todas_las_medidas():
    salida = resumen([1, 2, 3])
    assert salida == {"n": 3, "media": 2, "mediana": 2, "min": 1, "max": 3}


def test_resumen_de_un_solo_dato():
    salida = resumen([7])
    assert salida["min"] == salida["max"] == 7


def test_atipicos_pilla_el_bicho():
    assert atipicos([1, 2, 3, 4, 100]) == [100]


def test_atipicos_no_ve_nada_raro():
    assert atipicos([1, 2, 3, 4]) == []


def test_atipicos_los_da_en_el_orden_de_entrada():
    assert atipicos([100, 1, 2, 3, 4, 5, 6, 7, 8, 200]) == [100, 200]
