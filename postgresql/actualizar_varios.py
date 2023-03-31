import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:   # with cierra el recurso del cursor
            datos = (
                ("jonathan", "morales", "blonder413@outlook.com", 1),
                ("yulian", "gonzález", "bridyith@hotmail.com", 2)
            )
            sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            cursor.executemany(sql, datos)
            
            registros_actualizados = cursor.rowcount
            print(f'Se actualizaron {registros_actualizados} registros')
except Exception as e:
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
