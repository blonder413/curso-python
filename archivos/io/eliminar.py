import os
import os.path
import pathlib
# ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
ruta = os.path.abspath('./') + '/archivo.txt'
# ruta = '/var/www/html/index.html'

# if os.path.isfile(ruta):
#     os.remove(ruta)
# else:
#     print('no existe el fichero')

try:
    os.remove(ruta)
except FileNotFoundError:
    print('no existe el fichero')
except PermissionError:
    print('No tiene permisos sobre el directorio')
