class Constantes:
    @property
    def PI(self):  # aquí definimos la constante
        return 3.141592


constantes = Constantes()  # instanciamos el objeto Constantes

print(constantes.PI)  # accedemos a la constante PI

constantes.PI = 10  # intentamos alterar la constante