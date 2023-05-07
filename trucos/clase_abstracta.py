'''
ABC Abstract Base Class
Permite asegurar que las clases que las heredan implementen los métodos
'''
from abc import ABCMeta, abstractmethod

class ClaseBase(metaclass=ABCMeta):
    @abstractmethod
    def metodo1(self):
        pass

    @abstractmethod
    def metodo2(self):
        pass


class ClaseConcreta(ClaseBase):
    def metodo1(self):
        print("Método 1")


# obj = ClaseBase() # no es posible instanciar una clase abstracta
obj = ClaseConcreta()   # debe sobreescribir todos los métodos
print(obj)