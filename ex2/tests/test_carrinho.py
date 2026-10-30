from carrinho import total_com_desconto


def test_total_exato():
    assert total_com_desconto([10, 20, 30, 40, 50]) == 141.0

def test_arredondamento():
    assert total_com_desconto([10, 20, 30, 10.557]) == 69.50

def test_preco_negativo():
    assert total_com_desconto([10, -5, 20, 40]) == 61.0