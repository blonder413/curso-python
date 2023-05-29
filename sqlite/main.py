import os
import sqlite3

ruta = os.path.dirname(os.path.abspath(__file__))
cx = sqlite3.connect(ruta + '/agenda.db')  # Crear el archivo
cu = cx.cursor()    # Crear un cursor para la conexión

# cu.execute("create table if not exist agenda(id, nombre, celular, correo)") # Crear la tabla

sql_crear = '''
    create table if not exists agenda(
        id integer primary key autoincrement,
        nombre varchar(100),
        celular varchar(100),
        correo varchar(100)
    )
'''
cu.execute(sql_crear) # Crear la tabla

# Insertar registros
cu.execute("insert into agenda values (?, ?, ?, ?)", (None, "Rebecca", "5553943834", "rchambers@stars.gov"))

contactos = [
    (None, "Leon", "555043455", "lskennedy@rcpd.org"),
    (None, "Claire", "555384794", "credfield@terrasave.org")
]
cu.executemany("insert into agenda values (?, ?, ?, ?)", contactos)

cx.commit()
# execute a query and iterate over the result
for row in cu.execute("select * from agenda"):
    print(f'{row[0]}', end=' | ')
    print(f'{row[1]}', end=' | ')
    print(f'{row[2]}', end=' | ')
    print(f'{row[3]}')


cu.execute('DELETE FROM agenda WHERE id = 2')
cx.commit()
print('-'.center(50, '-'))

cu.execute("select * from agenda")
productos = cu.fetchall()
for value in productos:
    print(f'{value[0]}', end=' | ')
    print(f'{value[1]}', end=' | ')
    print(f'{value[2]}', end=' | ')
    print(f'{value[3]}')

cu.execute('select * from agenda where id = 8')
primero = cu.fetchone()
print(primero)

cx.close()  # Cerrar la conexión
