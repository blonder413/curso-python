# son un conjunto de sets
# son mutables

# -
print('set'.center(20, '-'))
usuario = {'jonathan', 'morales', '1985-04-13', 1.68}
usuario.add('blonder413@gmail.com')
usuario.discard('jonathan')     # Elimina un elemento sin lanzar excepción
usuario.remove('1985-04-13')    # Elimina un elemento, lanza excepción si no encuentra el elemento
print(usuario)
print(type(usuario))
# ---------------------------------------------------
print('diccionario'.center(20, '-'))
persona = {
    'nombre': 'jonathan',
    'fecha_nacimiento': '1985-04-13',
    'profesion': 'ingeniero de sistemas',
    'estatura': 1.68
    }
persona['vivo'] = True
persona.pop('fecha_nacimiento')
print(persona)
print(persona['nombre'])
print(persona.get('estatura'))
print(type(persona))
for indice, value in persona.items():
    print(f'key: {indice} - value {value}')

for indice in persona.keys():
    print(f'key: {indice}')

for value in persona.values():
    print(f'value {value}')

print('id' in persona)

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