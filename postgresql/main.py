import psycopg2

# Conectarse
cx = psycopg2.connect(database='agenda', user='blonder413', password='Mono/1985')
cu = cx.cursor()

# Insertar registros
datos = ("anyi", "acmendezmelo@gmail.com", "3108329850")
cu.execute("insert into agenda (nombre, correo, celular) values (%s, %s, %s)", datos)

cx.commit()


cu.execute("select * from agenda")
productos = cu.fetchall()
for value in productos:
    print(f'{value[0]}', end=' | ')
    print(f'{value[1]}', end=' | ')
    print(f'{value[2]}', end=' | ')
    print(f'{value[3]}')

cu.execute('select * from agenda where id = 2')
primero = cu.fetchone()
print(primero)

cx.close()  # Cerrar la conexión
