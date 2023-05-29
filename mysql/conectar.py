'''
nos conectamos a la base de datos
'''
# pip install mysql-connector-python
import mysql.connector

try:
    '''
    database = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='cursos',
        passwd='Cursos@Blonder413',
        database='cursos_agenda'
    )
    '''
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'cursos',
        'passwd': 'Cursos@Blonder413',
        'database': 'cursos_agenda'
    }
    database = mysql.connector.connect(**config)
except Exception as e:
    print(e)

try:
    cu = database.cursor(buffered=True)
except NameError as e:
    print(e)
