from logger_base import log
import psycopg2 as bd
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'blonder413'
    __PASSWORD = 'Mono/1985'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None

    @classmethod
    def obtener_conexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = bd.connect(host=cls.__HOST, user=cls.__USERNAME, password=cls.__PASSWORD, 
                                            port=cls.__DB_PORT, database=cls.__DATABASE)
                log.debug(f'Conexión exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                log.error(f'Ocurrió una excpeción al obtener la conexión {e}')
                sys.exit()
        else:
            return cls.__conexion
    
    @classmethod
    def obtener_cursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtener_conexion().cursor()
                log.debug(f'se abrió correctamente el cursor: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                log.error(f'Ocurrió una excepción al obtner el cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor

if __name__ == '__main__':
    Conexion.obtener_conexion()
    Conexion.obtener_cursor()
