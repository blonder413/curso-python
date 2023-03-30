import os
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

try:
    archivo = open(ruta + '/prueba.txt', 'r', encoding='utf8')

    for linea in archivo.readlines():
        print(linea)
except Exception as e:
    print(e)
