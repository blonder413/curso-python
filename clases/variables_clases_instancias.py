class Perro:
    patas = 4   # variable de clase

    def __init__(self, nombre):
        self.nombre = nombre    # variable de instancia (del objeto)


if __name__ == '__main__':
    perro1 = Perro('perro 1')
    perro2 = Perro('perro 2')
    Perro.patas = 5

    # No es posible acceder a las variables de instancia directamente desde la clase
    #print(Perro.nombre)

    # se crea una variable de instancia y oculta la variable de clase
    perro1.patas = 10
    
    Perro.nombre = 'Perrito'    # se crea una variable de clase
    
    print(Perro.patas, Perro.nombre)
    print(perro1.nombre, perro1.patas, perro1.__class__.patas)
    print(perro2.nombre, perro2.patas, perro2.__class__.patas)

    Perro.orejas = 2
    print(perro1.orejas, perro2.orejas, Perro.orejas)
