class Fila:
    def __init__(self):
        self._contador_normal = 0

    def emitir(self, tipo):
        self._contador_normal += 1
        return f"N{self._contador_normal}"
