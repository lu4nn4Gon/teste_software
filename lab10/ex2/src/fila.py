class Fila:
    def __init__(self):
        self._contador_normal = 0
        self._contador_prioritaria = 0
        self._normais = []
        self._prioritarias = []
        self._prioritarias_seguidas = 0

    def emitir(self, tipo):
        if tipo == "prioritaria":
            self._contador_prioritaria += 1
            senha = f"P{self._contador_prioritaria}"
            self._prioritarias.append(senha)
            return senha

        if tipo == "normal":
            self._contador_normal += 1
            senha = f"N{self._contador_normal}"
            self._normais.append(senha)
            return senha

        raise ValueError("Tipo de senha invalido")

    @property
    def aguardando(self):
        return len(self._normais) + len(self._prioritarias)

    def chamar(self):
        if self._normais and self._prioritarias_seguidas >= 2:
            self._prioritarias_seguidas = 0
            return self._normais.pop(0)

        if self._prioritarias:
            self._prioritarias_seguidas += 1
            return self._prioritarias.pop(0)

        if self._normais:
            self._prioritarias_seguidas = 0
            return self._normais.pop(0)

        raise IndexError("Fila vazia")
