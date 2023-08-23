"""
Las clases abstractas con métodos abstractos no se pueden instanciar
Para definir una clase abstracta debe heredar de ABC (Abstract Base clase)
"""
from abc import ABC, abstractmethod


class Abstracta(ABC):
    @abstractmethod
    def metodo_abstracto(self):
        '''`
        al agregar un método abstracto, la clase debe ser abstracta
        Para definir el método abstracto debemos usar el decorador y no ponerle cuerpo
        '''
        pass


class Hija(Abstracta):
    def metodo_abstracto(self):
        '''
        Este método debe sobreescribirse ya que al ser abstractos en la clase padre es obligatorio
        '''
        return 'se debe definir por heredar de una clase abstracta'


# abstracta = Abstracta()
hija = Hija()
