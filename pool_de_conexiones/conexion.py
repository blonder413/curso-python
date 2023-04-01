from logger_base import log
from psycopg2 import pool
import sys

class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'blonder413'
    __PASSWORD = 'Mono/1985'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtener_pull(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON, cls.__MAX_CON, host=cls.__HOST, user=cls.__USERNAME, password=cls.__PASSWORD, 
                    port=cls.__DB_PORT, database=cls.__DATABASE
                )
                log.debug(f'Creación del pool existosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                log.error(f'Error: {e}')
                sys.exit()
        else:
            return cls.__pool

    @classmethod
    def obtener_conexion(cls):
        conexion = cls.obtener_pull().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberar_conexion(cls, conexion):
        cls.obtener_pull().putconn(conexion)
        log.debug(f'Regresamos la conexion al pull: {conexion}')
    
    @classmethod
    def cerrar_conexiones(cls):
        cls.obtener_pull().closeall()

if __name__ == '__main__':
    conexion1 = Conexion.obtener_conexion()
    Conexion.liberar_conexion(conexion1)
    conexion2 = Conexion.obtener_conexion()
    conexion3 = Conexion.obtener_conexion()
    conexion4 = Conexion.obtener_conexion()
    conexion5 = Conexion.obtener_conexion()
    conexion6 = Conexion.obtener_conexion()
