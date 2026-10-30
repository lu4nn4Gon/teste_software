def parcela(valor, n):
    if n < 1 or n > 12:
        raise ValueError("Numero de parcelas invalido")

    if n <= 3:
        total = valor
    else:
        total = valor * (1 + 0.02 * (n - 3))

    return round(total / n, 2)