"""
Para eliminar un registro es necesario llamar al commit
python3 mysql/eliminar_registro_2.py 
"""

from conectar import database

try:
    with database:
        with database.cursor() as cursor:  # with cierra el recurso del cursor
            # Eliminar registro
            SQL = "DELETE FROM agenda WHERE id = %s"
            datos = (5,)
            cursor.execute(SQL, datos)

            SQL = "DELETE FROM agenda WHERE id IN (%s, %s)"
            datos = (6, 7)
            cursor.execute(SQL, datos)

            database.commit()

            # El primer registro se elimina pero no se cuenta, solo cuenta el último commit
            registros_eliminados = cursor.rowcount
            print(f"Se eliminaron {registros_eliminados} registros")
except Exception as e:
    print(e)
finally:
    database.close()  # Cerrar la conexión
