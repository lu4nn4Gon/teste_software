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


def test_quantidade_aguardando():
    fila = Fila()

    assert fila.aguardando == 0

    fila.emitir("normal")
    assert fila.aguardando == 1

    fila.emitir("prioritaria")
    assert fila.aguardando == 2


def test_ordem_atendimento_normal():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("normal")
    fila.emitir("normal")

    assert fila.chamar() == "N1"
    assert fila.chamar() == "N2"
    assert fila.chamar() == "N3"
    assert fila.aguardando == 0


def test_prioridade_atendimento():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "N1"
    assert fila.aguardando == 0


def test_limite_duas_prioritarias():
    fila = Fila()

    fila.emitir("normal")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")
    fila.emitir("prioritaria")

    assert fila.chamar() == "P1"
    assert fila.chamar() == "P2"
    assert fila.chamar() == "N1"
    assert fila.chamar() == "P3"
    assert fila.aguardando == 0
