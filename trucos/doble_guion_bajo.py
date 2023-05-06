class Padre():
    def __init__(self):
        self.__variable_privada = 3

    def get_variable_privada(self):
        return self.__variable_privada


class Hijo(Padre):
    def __init__(self):
        super().__init__()
        self.__variable_privada ='sobreescrita 3'

    def __privado(self):
        return 'privado'


_Prueba__variable_global = 'hola blonder'

class Prueba():
    def prueba(self):
        return __variable_global

if __name__ == '__main__':
    padre = Padre()
    print(dir(padre))
    print(f'name mangling: {padre._Padre__variable_privada}')
    print(padre.get_variable_privada())

    hijo = Hijo()
    print(f'Privada hijo: {hijo._Hijo__variable_privada}')
    print(f'Privada padre desde hijo: {hijo._Padre__variable_privada}')
    print(hijo._Hijo__privado())
    prueba = Prueba()
    print(prueba.prueba())
