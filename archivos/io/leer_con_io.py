from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
# r lee el archivo
archivo = open(ruta, 'r')
print(ruta)

# Leer
# contenido = archivo.read()
# print(contenido)

contenido = archivo.readlines()
archivo.close()
for linea in contenido:
    print(linea, end='')
