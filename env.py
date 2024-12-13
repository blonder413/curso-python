# pip3 install python-dotenv
# pip3 install python-decouple
# debemos crear el archivo .env en la raíz de nuestro proyecto
from decouple import config

nombre = config("NOMBRE")
print(nombre)
