import os
import shutil
nombre_carpeta = './mi_carpeta'

# crear directorio
if not os.path.isdir(nombre_carpeta):
    os.mkdir(nombre_carpeta)
else:
    print('ya existe el directorio')

# eliminar
# os.rmdir(nombre_carpeta)

# copiar
ruta = './mi_carpeta'
ruta_nueva = './mi_carpeta_copiada'
try:
    shutil.copytree(ruta, ruta_nueva)
except FileExistsError:
    print('ya existe')

# listar
contenido = os.listdir('./')
for archivo in contenido:
    print(archivo)
