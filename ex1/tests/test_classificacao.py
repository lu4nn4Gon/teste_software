import pytest
from classificacao import classificar_aluno


def test_aluno_aprovado():
    assert classificar_aluno(8.0, 80) == "Aprovado"


def test_aluno_reprovado():
    assert classificar_aluno(3.0, 90) == "Reprovado"

def test_media_zero():
    assert classificar_aluno(0, 80) == "Reprovado"


def test_media_dez():
    assert classificar_aluno(10, 80) == "Aprovado"


def test_media_sete():
    assert classificar_aluno(7.0, 80) == "Aprovado"


def test_media_cinco():
    assert classificar_aluno(5.0, 80) == "Recuperacao"

def test_reprovado_por_falta():
    assert classificar_aluno(8.0, 74) == "Reprovado por falta"


def test_presenca_limite():
    assert classificar_aluno(8.0, 75) == "Aprovado"


def test_presenca_cem():
    assert classificar_aluno(8.0, 100) == "Aprovado"

def test_media_negativa():
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(-1, 80)


def test_media_acima_dez():
    with pytest.raises(ValueError, match="^Media invalida$"):
        classificar_aluno(11, 80)


def test_presenca_negativa():
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8, -1)


def test_presenca_zero():
    assert classificar_aluno(8, 0) == "Reprovado por falta"


def test_presenca_acima_cem():
    with pytest.raises(ValueError, match="^Presenca invalida$"):
        classificar_aluno(8, 101)