class Padre:
    def __init__(nombre):
        pass

    def saludar(self):
        return 'soy la clase padre'

class Madre:
    def __init__(nombre):
        pass

    def saludar(self):
        return 'soy la clase madre'

class Hija(Padre, Madre):
    '''
    Se deben indicar el nombre de las clases padre entre paréntesis y separadas por coma
    Permite acceder a los atributos y métodos protected y public de las clases padre
    En caso de la herencia múltiple con métodos iguales se llamará a la clase nombrada primero en el paréntesis
    '''
    Padre.__init__('padre')
    Madre.__init__('madre')

hija = Hija()
print(hija.saludar())
print(Hija.mro())   # Method Resolution Order
