from io import open
import shutil
import pathlib

nombre_archivo = 'archivo.txt'
ruta = str(pathlib.Path().absolute()) + '/' + nombre_archivo

nuevo_nombre = 'nuevo.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/' + nuevo_nombre
ruta_alternativa = '../copiado.txt'
# shutil.copyfile(ruta, ruta_nueva)
shutil.copyfile(ruta, ruta_alternativa)
print('copiado')
