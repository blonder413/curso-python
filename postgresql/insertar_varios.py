import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:   # with cierra el recurso del cursor
            datos = (
                ("yeimmy", "salazar", "kateri346@hotmail.com"),
                ("rodrigo", "marin", "rodrimarin16@hotmail.com")
            )
            sql = 'INSERT INTO persona (nombre, apellido, email) VALUES (%s, %s, %s)'
            cursor.executemany(sql, datos)
            #conexion.commit()  # No es necesario si usamos el bloque with
            registros_insertados = cursor.rowcount
            print(f'Se insertaron {registros_insertados} registros')
except Exception as e:
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
