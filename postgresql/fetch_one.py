import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:   # with cierra el recurso del cursor
            # Listar registros
            sql = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = (2,)
            cursor.execute(sql, id_persona)
            registro = cursor.fetchone()
            print(registro)
except Exception as e:
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
