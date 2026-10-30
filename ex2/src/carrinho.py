def total_com_desconto(precos):
    total = 0.0

    for i, preco in enumerate(precos):
        if i >= 3:
            total += preco * 0.90
        else:
            total += preco

    return round(total, 2)