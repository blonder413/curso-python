"""
Una lista puede contener otras listas, esto genera una lista de múltiples dimensiones
"""
print('multidimensionales'.center(20, '-'))
contactos = [   # el corchete debe ir en esta línea
    ['albert', 'awesker@stars.gov'],
    ['alex', 'awesker@revelations2.game']
]

for value in contactos:
    print(f'nombre: {value[0]} - correo: {value[1]}', end='')
    print()

numeros = [
    [1, 2, 3, 4, 5],
    [2, 4, 6, 8],
    [1, 3, 5, 7, 9]
]

for numero in numeros:
    for i in numero:
        print(i)
    print("---")
