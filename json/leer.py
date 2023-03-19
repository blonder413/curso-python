import json

ruta = '/home/blonder413/Python/biblioteca-python/json/'
try:
    with open(ruta + 'archivo_json.json') as file:
        datos = json.load(file)

    for dato in datos['persona']:
        print(f"id: {dato['id']}", end=' | ')
        print(f"nombre: {dato['nombre']}", end=' | ')
        print(f"correo: {dato['correo']}", end=' | ')
        print()
        print('-'.center(55, '-'))
except FileNotFoundError as e:
    print('el archivo no existe')
