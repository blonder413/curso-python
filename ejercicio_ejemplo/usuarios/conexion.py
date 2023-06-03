import mysql.connector

def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user='cursos',
        password="Cursos@blonder413",
        database="master_python",
        port=3306
    )

    # buffered permite hacer muchas consultas usando el mismo cursor
    cu = database.cursor(buffered=True)
    return database, cu
