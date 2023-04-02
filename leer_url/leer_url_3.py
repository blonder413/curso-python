import urllib.request
from urllib.request import urlopen

# si da error 406, de lo contrario solo se pasa la url al método urlopen
req = urllib.request.Request(
    "http://globalmentoring.com.mx/recursos/GlobalMentoring.txt",
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    },
)

palabras = []
with urlopen(req) as mensaje:
    contenido = mensaje.read().decode('utf-8')

# print(contenido.count('Universidad'))
# print(contenido.upper()) # genera una nueva cadena, str es inmutable
# print(contenido.lower()) # genera una nueva cadena, str es inmutable
print('python' in contenido.lower()) # pregunta si existe la cadena python en el archivo
print(contenido.startswith('hola'.lower()))
print(contenido.endswith('mx'.lower()))
