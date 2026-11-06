def contar_palavras(texto):
    if not texto:
        return {}

    palavras = texto.lower().split()
    contagem = {}

    for palavra in palavras:
        palavra = palavra.strip(".,;:!?")

        if palavra:
            contagem[palavra] = contagem.get(palavra, 0) + 1

    return contagem
