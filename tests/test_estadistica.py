import pytest

from estadistica import media


def test_media():
    assert media([1, 2, 3]) == 2


def test_media_con_decimales():
    assert round(media([1, 2]), 3) == 1.5


def test_media_de_nada():
    with pytest.raises(ValueError):
        media([])
