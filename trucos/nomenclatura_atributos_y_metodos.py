from modulo_protegidas import _protegida

class NomenclaturaAtributosYMetodos():
    def __init__(self):
        self.variable = 4
        self._protegida = 13


if __name__ == '__main__':
    objeto = NomenclaturaAtributosYMetodos()
    # no se deberían acceder a variables con _ al inicio
    print(objeto._protegida)
    _protegida()

