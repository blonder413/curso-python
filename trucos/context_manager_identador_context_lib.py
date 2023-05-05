from contextlib import contextmanager

class ContextManagerIdentadorContextLib():
    def __init__(self):
        self.nivel = 0

    @contextmanager
    def identador(self):
        try:
            self.nivel += 1
            yield self
        finally:
            self.nivel -= 1
    
    def imprimir(self, texto):
        print(' '*self.nivel + texto)


if __name__ == '__main__':
    objeto = ContextManagerIdentadorContextLib()
    with objeto.identador():
        objeto.imprimir('nivel 1')
        with objeto.identador():
            objeto.imprimir('nivel 2')
        objeto.imprimir('primer nivel')
