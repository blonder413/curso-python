import os
import shutil

ruta_archivo = os.path.abspath(__file__)
ruta = os.path.dirname(ruta_archivo)

pwd = os.getcwd()

# Crear directorios
nombre_directorio = 'nuevo_directorio'
if not os.path.isdir(ruta + '/' + nombre_directorio):
    os.mkdir(ruta + '/' + nombre_directorio)
else:
    print(f'el directorio {nombre_directorio} no se creó porque ya existe')

# Renombrar directorios
if not os.path.isdir(ruta + '/' + 'renombrado'):
    os.rename(ruta + '/' + nombre_directorio, ruta + '/renombrado')
else:
    print(f'el directorio renombrado ya existe')

# Eliminar directorios
if os.path.isdir(ruta + '/' + nombre_directorio):
    os.rmdir(ruta + '/' + nombre_directorio)
    print(f'Se eliminó {nombre_directorio}')
else:
    print(f'no se puede eliminar {nombre_directorio} porque no existe')

# Eliminar directorios de forma recursiva
if os.path.isdir(ruta + '/' + nombre_directorio):
    shutil.rmtree(ruta + '/' + nombre_directorio)
    print(f'Se eliminó el directorio {nombre_directorio}')
else:
    print(f'No se eliminó el directorio {nombre_directorio}')

print(os.listdir(ruta))

# Copiar
shutil.copy(ruta + '/hola.html', ruta + '/nuevo.html')
# Mover
shutil.move(ruta + '/nuevo.html', ruta + '/movido.html')
