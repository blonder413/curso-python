import requests
import re

url = 'http://localhost/pagina/productos.php'
response = requests.get(url)

if response.status_code == 200:
    contenido = response.text
else:
    print(response.status_code)


regex = '<div class="precio">(.+?)</div>'   # etiqueta donde se va a extraer el contenido

for value in re.findall(regex, contenido): # contenido es donde están los datos
    print(value)
    print(value[1:len(value)])   # Omitir el primer caracter