import ftplib
import os

ruta = os.path.dirname(os.path.abspath(__file__))   # Ruta del archivo actual

try:
    ftp = ftplib.FTP('192.168.0.1', 'usuario', 'clave') # Conexión
    print(ftp.dir())    # Listar archivos
    ftp.retrbinary('hola.py', open(ruta + '/descargado.py', 'wb').write) # Descargar
    ftp.storbinary('STOR' + 'archivo.py', open(ruta + '/archivo.py', 'rb'))  # Subir

except ConnectionRefusedError as e: # Error en la conexión
    print(e.strerror)