import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:   # with cierra el recurso del cursor
            # Listar registros
            sql = 'SELECT * FROM persona'
            cursor.execute(sql)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
