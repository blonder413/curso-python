import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

try:
    conexion.autocommit = False
    cursor = conexion.cursor()
    sql = 'INSERT INTO persona(nombre, apellido, email) values(%s, %s, %s)'
    datos = ('yamel', 'campos', 'andreilla810@gmail.com')
    cursor.execute(sql, datos)

    sql = 'DELETE FROM persona WHERE id_persona = %s'
    datos = (413,)
    cursor.execute(sql, datos)

    sql = 'UPDATE persona SET apellido = %s WHERE id_persona = %s'
    datos = ('morales salazar', 1)  # generamos error
    cursor.execute(sql, datos)

    conexion.commit()
except Exception as e:
    conexion.rollback()
    print(e)
finally:
    conexion.close()    # Cerrar la conexión
