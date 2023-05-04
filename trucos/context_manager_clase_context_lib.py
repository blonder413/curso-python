from contextlib import contextmanager
import os

'''
creamos un generador que adquiere el recurso y posteriormente suspende la ejecución al utilizar yield
cuando termina de ser utilizado el método, regresa la ejecución y cierra el recurso
'''
@contextmanager
def manejador_archivos(nombre):
    try:
        archivo = open(nombre, 'w', encoding='utf8')
        yield archivo
    finally:
        archivo.close()


if __name__ == '__main__':
    ruta_archivo = os.path.abspath(__file__)
    ruta = os.path.dirname(ruta_archivo)
    with manejador_archivos(ruta + '/prueba.txt') as archivo:
        archivo.write('context manager desde contextlib')
        archivo.write('\nel yield mantiene el recurso abierto')
