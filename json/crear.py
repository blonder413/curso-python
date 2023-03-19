import json

ruta = '/home/blonder413/Python/biblioteca-python/json/'
data = {}
data['persona'] = []
data['persona'].append({
    'id': 1,
    'nombre': 'jonathan',
    'correo': 'blonder413@gmail.com',
    'vivo': True
})
data['persona'].append({
    'id': 2,
    'nombre': 'bridyith',
    'correo': 'bridyith@hotmail.com',
    'vivo': True
})

try:
    with open(ruta + 'archivo_json.json', 'w') as file:
        json.dump(data, file, indent=4)
except PermissionError as e:
    print('No tiene permisos para escribir en el directorio indicado')
except FileNotFoundError as e:
    print("El directorio indicado no existe")
