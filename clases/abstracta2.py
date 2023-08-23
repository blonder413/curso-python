"""
Las clases abstractas con métodos abstractos no se pueden instanciar
si no se define algún decorador abstractmethod sí permite que se instancie
"""
import abc


class Abstracta(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def metodo_abstracto(self):
        pass

    def saludar(self):
        return "hola blonder"


if __name__ == '__main__':
    abstracta = Abstracta()
    print(abstracta.saludar())
    print(abstracta)
