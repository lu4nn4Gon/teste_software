import pytest
from parcelamento import parcela


def test_sem_juros():
    assert parcela(300, 3) == 100.00


def test_com_juros():
    assert parcela(400, 4) == 102.00


def test_parcelas_invalidas():
    with pytest.raises(ValueError):
        parcela(300, 0)

def test_uma_parcela():
    assert parcela(300, 1) == 300.00


def test_cinco_parcelas():
    assert parcela(500, 5) == 104.00


def test_arredondamento():
    assert parcela(100, 3) == 33.33


def test_mensagem_erro():
    with pytest.raises(ValueError, match="^Numero de parcelas invalido$"):
        parcela(300, 13)

def test_doze_parcelas():
    assert parcela(1200, 12) == 118.00