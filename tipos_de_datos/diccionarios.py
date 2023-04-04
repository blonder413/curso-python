# son un conjunto de sets
# son mutables, pero las llaves no pueden ser mutables
# tienen un orden, los sets no
# ---------------------------------------------------
from pprint import pprint as pp
print('diccionario'.center(20, '-'))
persona = {
    'nombre': 'jonathan',
    'fecha_nacimiento': '1985-04-13',
    'profesion': 'ingeniero de sistemas',
    'estatura': 1.68
    }
persona['vivo'] = True
persona.pop('fecha_nacimiento')
print(persona['nombre'])    # KeyError si no encuentra la llave
print(persona.get('estatura'))
print(persona.get('altura', 'No existe la llave'))
edad = persona.setdefault('edad', 38)   # Asigna un valor si no existe la llave
print(persona)
print(type(persona))
for indice, value in persona.items():
    print(f'key: {indice} - value {value}')

for indice in persona.keys():
    print(f'key: {indice}')

for value in persona.values():
    print(f'value {value}')

print('id' in persona)

pp(persona)
pp(persona, sort_dicts=False)

persona.clear() # Elimina toda la información del diccionario
del persona # Elimina la variable
# ---------------------------------------------------
print('lista de diccionarios'.center(50, '-'))
contactos = [
    {'nombre': 'jonathan', 'correo': 'blonder413@gmail.com'},
    {'nombre': 'bridyith', 'correo': 'bridyith@hotmail.com'}
]
print(type(contactos))
print(type(contactos[0]))
