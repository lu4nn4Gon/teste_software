class Fila:
    def __init__(self):
        self._contador_normal = 0
        self._contador_prioritaria = 0

    def emitir(self, tipo):
        if tipo == "prioritaria":
            self._contador_prioritaria += 1
            return f"P{self._contador_prioritaria}"

        self._contador_normal += 1
        return f"N{self._contador_normal}"
