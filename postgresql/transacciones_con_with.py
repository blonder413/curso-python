import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sql = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
            datos = ('anyi', 'mendez', 'acmendezmelo@gmail.com')
            cursor.execute(sql, datos)

            sql = 'DELETE FROM persona WHERE id_persona = %s'
            datos = (413,)
            cursor.execute(sql, datos)

            sql = 'UPDATE persona SET apellido = %s WHERE id_persona = %s'
            datos = ('morales salazar', 1)  # generamos error
            cursor.execute(sql, datos)
except Exception as e:
    print(e)    # No es necesario agregar rollback si se usa with
finally:
    conexion.close()    # Cerrar la conexión
