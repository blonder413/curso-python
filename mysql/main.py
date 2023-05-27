from conectar import database, cu

cear_tabla = '''
create table if not exists agenda(
    id int not null auto_increment primary key,
    nombre varchar(100),
    correo varchar(100),
    fecha_nacimiento date
);
'''
cu.execute(cear_tabla)

# Crear registro
#cu.execute("insert into agenda values (%s, %s, %s, %s)", (None, "Jonathan", "blonder413@gmail.com", "1985-04-13"))


datos = [
    (None, "Jill", "jvalentine@stars.gov", "1986-10-08"),
    (None, "Chris", "credfieldd@bsaa.org", "1990-08-17")
]
#cu.executemany("insert into agenda values (%s, %s, %s, %s)", datos)

database.commit()

cu.execute("select * from agenda")
productos = cu.fetchall()
for value in productos:
    print(f'{value[0]}', end=' | ')
    print(f'{value[1]}', end=' | ')
    print(f'{value[2]}', end=' | ')
    print(f'{value[3]}')

cu.execute('select * from agenda where id = 4')
primero = cu.fetchone()
print(f'id: {primero[0]}', end=' | ')
print(f'nombre: {primero[1]}', end=' | ')
print(f'correo: {primero[2]}', end=' | ')
print(f'fecha nacimiento: {primero[3]}')

database.close()
