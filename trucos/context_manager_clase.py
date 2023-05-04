'''
Context manager en clases
1. sobreescribimos las funciones __enter__ y __exit__
2. utilizando la biblioteca contextlib
'''
import os

class ContextManagerClase():
    def __init__(self, nombre):
        self.nombre = nombre
    

    def __enter__(self):
        self.archivo = open(self.nombre, 'w', encoding='utf8')
        return self.archivo


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()


if __name__ == '__main__':
    # prueba implementando context manager
    
    ruta_archivo = os.path.abspath(__file__)
    ruta = os.path.dirname(ruta_archivo)
    # al entrar al bloque with se llama a __enter__
    with ContextManagerClase(ruta + '/prueba.txt') as archivo:
        archivo.write('context manager clases ñandú')
        # al terminar el bloque witch se llama __exit__
