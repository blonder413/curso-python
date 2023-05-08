class ContextManagerIdentador():
    def __init__(self):
        self.nivel = 0

    def __enter__(self):
        self.nivel += 1
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.nivel -= 1

    def imprimir(self, texto):
        print('  ' * self.nivel + texto)


if __name__ == '__main__':
    with ContextManagerIdentador() as identador:
        identador.imprimir('hola blonder')
        with identador:
            identador.imprimir('bye blonder')
