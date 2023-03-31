import psycopg2

conexion = psycopg2.connect(user = 'blonder413', password = 'Mono/1985', host = 'localhost', port = 5432, database = 'test_db')

cursor = conexion.cursor()

# Listar registros
sql = 'SELECT * FROM persona'
cursor.execute(sql)
registros = cursor.fetchall()

print(registros)

cursor.close()  # Cerrar el cursor
conexion.close()    # Cerrar la conexión
