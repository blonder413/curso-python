import pathlib

# definimos la ruta actual
ruta = pathlib.Path('.')

# mostramos los archivos con extensión py
for archivo in ruta.glob('*.py'):
    print(archivo)