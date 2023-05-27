# son un conjunto de sets
# son mutables, pero las llaves no pueden ser mutables
# tienen un orden, los sets no
# ---------------------------------------------------
from pprint import pprint as pp
print('diccionario'.center(20, '-'))
persona = {
    'nombre': 'juan',
    'fecha_nacimiento': '2050-04-13',
    'profesion': 'ingeniero de sistemas',
    'estatura': 1.68
    }
persona['vivo'] = True
persona.pop('fecha_nacimiento')
print(persona['nombre'])    # KeyError si no encuentra la llave
print(persona.get('estatura'))
print(persona.get('altura', 'No existe la llave'))
edad = persona.setdefault('edad', 18)   # Asigna un valor si no existe la llave
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
    {'nombre': 'blonder', 'correo': 'blonder@rgame.com'},
    {'nombre': 'juan', 'correo': 'juan@hotmail.com'}
]
print(type(contactos))
print(type(contactos[0]))

# Unir dos diccionarios
uno = {'nombre': 'nemesis', 'correo': 'nemesis@hotmail.com'}
dos = {'estatura': 1.68}

# tres = {**uno, **dos}   # No recomendado
tres = uno | dos

print(tres)

valores_al_cuadradado = {i: i*i for i in range(5)}
print(valores_al_cuadradado)
# lista = [1,2,3]
# diccionario_erroneo = {lista: 'a'}
tupla = (1,2,3)
diccionario = {tupla: 'a'}
print(diccionario)
