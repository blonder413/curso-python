"""
los logs son mensajes que podemos dejar de acuerdo al funcionamiento de nuestras app,
lo normal es dejarlos en archivos .log
En python existen varios niveles: DEBUG, ERROR
logging.NOTSET      0
logging.DEBUG       10
logging.INFO        20
logging.WARNING     30
logging.ERROR       40
logging.CRITICAL    50

Según el nivel definido se envían los logs de los niveles inferiores,
por ejemplo un nivel DEBUG enviará todos menos NOTSET,
mientras que un ERROR solo enviará los tipos ERROR y CRITICAL

# logging.handlers — Gestores de logging
# https://docs.python.org/es/3/library/logging.handlers.html#module-logging.handlers
- StreamHandler
- FileHandler
- NullHandler
"""
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# Guardar la información en un archivo
handler = logging.FileHandler('app.log')

# Dar formato a la información que se va a guardar
formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')
handler.setFormatter(formatter)

# Se pueden agregar varios handler
logger.addHandler(handler)

# Definimos un handler para mostrar información en consola
handler2 = logging.StreamHandler()
handler2.setFormatter(formatter)
logger.addHandler(handler2)

def ejemplo():
    logger.info('log de información')

if __name__ == '__main__':
    # ejemplo()
    logging.basicConfig(level=logging.DEBUG)
    logging.info('log de información')
