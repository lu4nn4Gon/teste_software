import pytest
from temperaturas import maior, dia_do_maior


def test_maior():
    assert maior([20, 25, 30, 22]) == 30


def test_dia_do_maior():
    assert dia_do_maior([20, 25, 30, 22]) == 2

def test_maior_primeira_posicao():
    assert maior([35, 20, 25]) == 35


def test_maior_segunda_posicao():
    assert maior([20, 35, 25]) == 35

def test_maior_lista_vazia():
    with pytest.raises(ValueError, match="^Lista vazia$"):
        maior([])


def test_dia_do_maior_lista_vazia():
    with pytest.raises(ValueError, match="^Lista vazia$"):
        dia_do_maior([])

def test_dia_maior_primeira_posicao():
    assert dia_do_maior([35, 20, 25]) == 0


def test_dia_maior_segunda_posicao():
    assert dia_do_maior([20, 35, 25]) == 1


def test_dia_maior_repetido():
    assert dia_do_maior([20, 30, 30]) == 1