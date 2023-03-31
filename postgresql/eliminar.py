import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:   # with cierra el recurso del cursor
            datos = (4,)
            sql = 'DELETE FROM persona WHERE id_persona = %s'
            cursor.execute(sql, datos)
            
            registros_eliminados = cursor.rowcount
            print(f'Se eliminaron {registros_eliminados} registros')
except Exception as e:
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
