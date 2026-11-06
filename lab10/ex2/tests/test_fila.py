import pytest

from fila import Fila


def test_primeira_senha_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"


def test_numeracao_senhas_normais():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("normal") == "N3"


def test_numeracao_senhas_prioritarias():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
    assert fila.emitir("prioritaria") == "P1"
    assert fila.emitir("normal") == "N2"
    assert fila.emitir("prioritaria") == "P2"


def test_tipo_invalido():
    fila = Fila()

    with pytest.raises(ValueError):
        fila.emitir("urgente")


def test_chamar_fila_vazia():
    fila = Fila()

    with pytest.raises(IndexError):
        fila.chamar()
