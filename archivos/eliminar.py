import os
archivo = 'prueba.txt'
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

os.remove(ruta + '/' + archivo)
