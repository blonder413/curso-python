from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
# a+ agrega contenido al final del archivo, si no existe lo crea
archivo = open(ruta, 'a+')
print(ruta)

# Escribir
archivo.write('Hola blonder\n')

# Cerrar archivo
archivo.close()
