import urllib.request
from urllib.request import urlopen

# si da error 406, de lo contrario solo se pasa la url al método urlopen
req = urllib.request.Request(
    "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)

with urlopen(req) as mensaje:
    contenido = mensaje.read().decode('utf-8')
    print(contenido)

# creamos un archivo nuevo con el resultado de la url
with open('nuevo_archivo.txt', 'w', encoding='utf-8') as archivo:
    archivo.write(contenido)
