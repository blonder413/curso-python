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

database.close()
