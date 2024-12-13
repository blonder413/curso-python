"""
Las variables de entorno son valores que se guardan dentro del propio sistema operativo
sirven para indicar valores generalmente a los intrépretes de línea de comandos.
Por ejemplo, cuando en GNU/Linux ejecutamos un comando como "ls" lo podemos hacer desde cualquier ubicación,
el sistema operativo se encarga de buscar internamente en las rutas guardadas en la variable de entorno PATH
donde se encuentra guardado el ejecutable ls.
Si en la terminal ponemos "echo $USER" se mostrará el nombre de nuestro usuario.
Para crear una variable de entorno en nuestro sistema operativo podemos ejecutar lo siguiente
export BD_PASSWORD="Mi password"
con esto crearemos una variable de entorno llamada BD_PASSWORD cuyo valor será "Mi password"
para ver dicho valor podemos escribir "printenv BD_PASSWORD"
Para eliminarla podemos usar "unset BD_PASSWORD"

En este ejemplo vamos a instalar el siguiente módulo para leer variables de entorno
pip3 install python-decouple
"""

import os
from decouple import config

try:
    password = os.environ["BD_PASSWORD"]
    print(password)
except Exception as error:
    print(f"Error. No existe la variable {error.args}")

