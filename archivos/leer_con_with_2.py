import os
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

try:
    with open(ruta + '/prueba.txt', 'r', encoding='utf8') as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            print(linea)
except Exception as e:
    print(e)
