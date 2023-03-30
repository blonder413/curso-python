'''
r   leer
a   agregar información a un archivo existente
w   escribir un archivo borrando todo si ya existe
x   crear un archivo y envía error si el archivo existe
r+  lectura y escritura
w+  lectura y escritura
'''
import os
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

try:
    archivo = open(ruta + '/prueba.txt', 'r', encoding='utf8')
    #print(archivo.read())   # Leer todo el archivo
    print(archivo.readline())   # Leer una línea
except Exception as e:
    print(e)
