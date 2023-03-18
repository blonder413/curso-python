class Padre:
    def saludar(self):
        return 'soy la clase padre'

class Madre:
    def saludar(self):
        return 'soy la clase madre'

class Hija(Padre, Madre):
    '''
    Se deben indicar el nombre de las clases padre entre paréntesis y separadas por coma
    Permite acceder a los atributos y métodos protected y public de las clases padre
    En caso de la herencia múltiple con métodos iguales se llamará a la clase nombrada primero en el paréntesis
    '''
    pass

hija = Hija()
print(hija.saludar())
