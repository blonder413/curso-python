import os
ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

try:
    archivo = open(ruta + '/prueba.txt', 'w', encoding='utf8')   # Creamos el archivo para escritura
    archivo.write('agregamos información al archivo')
    archivo.write('\nagregamos otra línea')
except Exception as e:
    print(e)
# finally:
#     archivo.close()
