def maior(temps):
    if not temps:
        raise ValueError("Lista vazia")

    maior_temp = temps[0]

    for temp in temps[1:]:
        if temp > maior_temp:
            maior_temp = temp

    return maior_temp


def dia_do_maior(temps):
    if not temps:
        raise ValueError("Lista vazia")

    indice_maior = 0

    for i in range(1, len(temps)):
        if temps[i] > temps[indice_maior]:
            indice_maior = i

    return indice_maior