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
    for linea in mensaje:
        # palabras_por_linea = linea.split()  # Retorna cada línea en tipo byte
        palabras_por_linea = linea.decode('utf-8').split()
        for palabra in palabras_por_linea:
            palabras.append(palabra)
    
print(palabras)
