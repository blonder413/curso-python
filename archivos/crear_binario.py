import os

ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)


def crear():
    try:
        archivo = open(ruta + '/prueba.bin', 'wb')  # Creamos el archivo para escritura
        archivo.write('agregamos información al archivo'.encode("utf-8"))
        archivo.write('\nagregamos otra línea'.encode("utf-8"))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    crear()
