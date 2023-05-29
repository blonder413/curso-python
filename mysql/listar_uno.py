from conectar import database, cu

print('listar un registro'.center(50, '-'))

cu.execute('select * from agenda where id = 1')
primero = cu.fetchone()
print(f'id: {primero[0]}', end=' | ')
print(f'nombre: {primero[1]}', end=' | ')
print(f'correo: {primero[2]}', end=' | ')
print(f'fecha nacimiento: {primero[3]}')

database.close()
