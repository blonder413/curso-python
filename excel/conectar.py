import mysql.connector
from mysql.connector import errorcode


# conexión a la base de datos
def conexion():
    try:
        return mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd="fcVBTgdRSYylkmIX",
            database="dad2"
        )
    except mysql.connector.Error as e:

        print(f"error de conexión: {e}")
        exit()


def getDatos(sql):
    cn = conexion()
    cur = cn.cursor(buffered=True)
    try:
        cur.execute(sql)

        return cur.fetchall()
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()


def getDato(sql):
    cn = conexion()
    cur = cn.cursor(buffered=True)
    try:
        cur.execute(sql)
        return cur.fetchone()
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()


def setDatos(sql):
    cn = conexion()
    cur = cn.cursor(buffered=True)
    try:
        cur.execute(sql)
        cn.commit()
    except mysql.connector.Error as e:
        print(f"error con la consulta: {e}")
        exit()
    cn.close()
