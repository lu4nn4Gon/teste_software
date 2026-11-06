from fila import Fila


def test_primeira_senha_normal():
    fila = Fila()
    assert fila.emitir("normal") == "N1"
