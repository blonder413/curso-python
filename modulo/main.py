import sys
import pathlib
ruta = str(pathlib.Path().absolute())
sys.path.append(ruta)

from paquete.variables_globales import archivo_nuevo

print(archivo_nuevo)
