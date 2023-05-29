from conectar import database, cu

print('listar todos los registros'.center(50, '-'))
cu.execute("select * from agenda")
productos = cu.fetchall()
for value in productos:
    print(f'{value[0]}', end=' | ')
    print(f'{value[1]}', end=' | ')
    print(f'{value[2]}', end=' | ')
    print(f'{value[3]}')

database.close()
