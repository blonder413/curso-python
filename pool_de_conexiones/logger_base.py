import logging as log

# Por defecto el nivel es WARNING

log.basicConfig(
    level= log.DEBUG, 
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt='%I:%I:%S %p', # Horas, minutos y segundos y am pm
    handlers= [
        log.FileHandler('capa_datos.log'),  # agregar información a un archivo
        log.StreamHandler() # Agregar información a la consola
    ]
)
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critical')
