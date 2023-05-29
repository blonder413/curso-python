"""
Para eliminar un registro es necesario llamar al commit
"""
from conectar import database, cu

print('eliminar un registro'.center(50, '-'))
cu.execute('DELETE FROM agenda WHERE id = %s', (6,))
print(cu.rowcount, 'registros borrados')
database.commit()

database.close()
