'''
__str__ su objetivo es que la información sea legible para el usuario. Su
implemetación por defecto llama al método __repr__
__repr__ su objetivo es que la información no sea ambigua, se usa para debug.
Tiene un formato tipo constructor
Cualquier colección usa __repr__ en lugar de __str__ para imprimir la
información
Si en una clase de define solo __repr__, al intentar llamar __str__ se llama a __repr__
'''
class Auto:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

# por defecto solo se muestra el nombre de la clase y el id del objeto
audi_a3 = Auto('audi', 'a3', 'amarillo')
print(audi_a3)

class AutoStr:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    def __str__(self):
        return f'str: {self.marca} {self.modelo} {self.color}'

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'{self.marca!r}, {self.modelo!r}, {self.color!r})')


auto_2 = AutoStr('carro', 'nuevo', 'yellow')
print(auto_2)   # no es necesario llamar a __str__
print(str(auto_2))
print('{}'.format(auto_2))
print(f'{auto_2}')

# Se recomienda usar __repr__ en lugar de __str__
# cuando se imprime una colección __repr__ tiene prioridad sobre __str__
print([auto_2])
print(f'{auto_2!r}')
print(str(auto_2))
print(repr(auto_2))
