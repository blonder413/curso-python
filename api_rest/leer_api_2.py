import json
import urllib.request

respuesta = urllib.request.urlopen('http://localhost/blog-yii-2-bootstrap-3/web/apirest/articulo')
# print(respuesta)

cuerpo_respuesta = respuesta.read()
# print(cuerpo_respuesta)

json_response = json.loads(cuerpo_respuesta.decode('utf-8'))

# print(json_response[0].get('titulo'))

for articulo in json_response:
    print(articulo['titulo'])
