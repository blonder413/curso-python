import pathlib

# definimos la ruta actual
ruta = pathlib.Path('.')

archivo = input("nombre del archivo a buscar: ")
archivo = ruta / archivo

# verificamos si existe el archivo
if archivo.exists():
    print(f'El archivo existe y pesa {archivo.stat().st_size} bytes')
else:
    print("No existe el archivo")
