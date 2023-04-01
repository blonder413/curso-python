from conexion import Conexion
from logger_base import log

class Cursor:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None
    
    def __enter__(self):    # se llama al empezar a usar el with
        log.debug(f'Inicio del método with')
        self.__conexion = Conexion.obtener_conexion()
        self.__cursor = self.__conexion.cursor()
        return self.__cursor
    def __exit__(self, tipo_exception, valor_excepcion, detalle_excepcion): # Se llama cuando termina el bloque with
        log.debug(f'Se ejecuta el método __exit__')
        if valor_excepcion:
            self.__conexion.rollback()
            log.error(f'Hubo un error: {valor_excepcion} {tipo_exception} {detalle_excepcion}. Se hace rollback')
        else:
            self.__conexion.commit()
            log.debug(f'Commit de la transacción')
        self.__cursor.close()
        Conexion.liberar_conexion(self.__conexion)

if __name__ == '__main__':
    with Cursor() as cursor:
        log.debug(f'dentro del bloque with')
        cursor.execute('SELECT * FROM persona')
        log.debug(cursor.fetchall())
