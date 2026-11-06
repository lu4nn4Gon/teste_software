def contar_palavras(texto):
    if not texto:
        return {}

    palavras = texto.lower().split()
    contagem = {}

    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem
