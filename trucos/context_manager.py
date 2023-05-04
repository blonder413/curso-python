import os
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

archivo = open(ruta + '/prueba.txt', 'w', encoding='utf8')
try:
    archivo.write('hola blonder')
finally:
    archivo.close()

# Código mejorado
with open(ruta + '/prueba.txt', 'w', encoding='utf8') as archivo:
    archivo.write('hola blonder')
