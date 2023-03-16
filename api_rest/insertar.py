"""Módulo para consumir la API"""
import requests

ENDPOINT = 'http://localhost/blog-yii-2-bootstrap-3/apirest/articulos'

payload = {
	"titulo": "Prueba desde python rest",
	"slug": "prueba-desde-python-rest",
	"detalle": "En este video veremos cómo instalar gajim en Ubuntu 20.04, veremos dónde podemos registrarnos en caso de no tener una cuenta.",
	"categoria_id": "1",
	"video": '<iframe src="https://video.hardlimit.com/videos/embed/be490fa3-9b77-418d-b11c-73e5ff004956" width="560" height="315" frameborder="0"></iframe>',
	"etiquetas": "xmpp,ubuntu,gajim",
	"resumen": "En este video veremos cómo instalar gajim en Ubuntu 20.04, veremos dónde podemos registrarnos en caso de no tener una cuenta.",
	"usuario_crea": "1",
	"estado": "1",
	"fecha_crea": "2023-03-18",
	"usuario_modifica": "1",
	"fecha_modifica": "2023-03-18",
}

response = requests.post(ENDPOINT, json=payload, timeout = 30)

print(response.text)