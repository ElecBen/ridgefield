import pytest

from estadistica import desviacion, media, mediana


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
