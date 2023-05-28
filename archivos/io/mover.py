'''
Para renombrar un archivo se debe mover con otro nombre
'''

import shutil
import pathlib
ruta = str(pathlib.Path().absolute()) + '/archivo.txt'
ruta_nueva = str(pathlib.Path().absolute()) + '/nuevo_archivo.txt'
shutil.move(ruta, ruta_nueva)
