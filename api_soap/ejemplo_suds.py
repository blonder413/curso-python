# pip install suds
from suds.client import Client
url = 'http://www.otravuelta.cl/soap/index.php?wsdl'
cliente = Client(url)   # consumir la API
resultados = cliente.service.retornarDatos() # Ejecutamos el método del endpoint
print(resultados)