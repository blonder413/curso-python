'''
Extensión del tipo tupla
alternativa para escribir clases con atributos inmutables
se puede asignar un identificador a cada uno de los elementos de la tupla
'''
from collections import namedtuple
Persona = namedtuple('Persona', 'nombre apellido edad')
p1 = Persona('Juan', 'Perez', 25)
# p1.nombre = 'blonder'
print(p1)
print(p1.nombre, p1.apellido, p1.edad)
Persona2 = namedtuple('Persona2', ['nombre', 'apellido', 'edad'])
p2 = Persona2('Juan', 'Perez', 25)
print(p2)
print(p2[0], p2[1], p2[2])

# unpacking
nombre, apellido, edad = p2
print(nombre, apellido, edad)
print(*p2)

# subclases de namedtuples
class Persona3(Persona2):
    def convertir_mayusculas(self):
        return f'Nombre: {self.nombre.upper()} {self.apellido.upper()}'

p3 = Persona3('Juan', 'Perez', 25)
print(p3.convertir_mayusculas())

# forma recomendada para heredar
Persona4 = namedtuple('Persona4', Persona2._fields + ('email',))
p4 = Persona4('Armando', 'Casas',4, 'armandocasas@email.com')
print(p4._fields)

# convertir  un diccionario
dict_p4 = p4._asdict()
print(dict_p4)
