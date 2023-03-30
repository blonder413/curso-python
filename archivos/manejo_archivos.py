import os

class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

    def __enter__(self):
        '''
        se llama al abrir el recurso
        '''
        print('obtenemos el recurso'.center(30, '-'))
        self.nombre = open(self.nombre, 'r', encoding='utf8')
        return self.nombre
    
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        '''
        Se llama cuando se terminan de ejecutar las líneas
        '''
        if self.nombre: # si existe el archivo está abierto
            print('se cierra el recurso'.center(30, '-'))
            self.nombre.close() # cerramos el archivo

ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

with ManejoArchivos(ruta + '/prueba.txt') as archivo:
    print(archivo.read())
