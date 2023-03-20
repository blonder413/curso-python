# son un conjunto de sets
# son mutables

# -
print('set'.center(20, '-'))
usuario = {'jonathan', 'morales', '1985-04-13', 1.68}
usuario.add('blonder413@gmail.com')
usuario.discard('jonathan')     # Elimina un elemento
usuario.remove('1985-04-13')    # Elimina un elemento
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
print(persona)
print(persona['nombre'])
print(type(persona))
# ---------------------------------------------------
print('lista de diccionarios'.center(50, '-'))
contactos = [
    {'nombre': 'jonathan', 'correo': 'blonder413@gmail.com'},
    {'nombre': 'bridyith', 'correo': 'bridyith@hotmail.com'}
]
print(type(contactos))
print(type(contactos[0]))