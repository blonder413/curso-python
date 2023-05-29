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
        passwd='cursos@Blonder413',
        database='blonder413'
    )
    '''
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'cursos',
        'passwd': 'cursos@Blonder413',
        'database': 'blonder413'
    }
    database = mysql.connector.connect(**config)
except Exception as e:
    print(e)

try:
    cu = database.cursor(buffered=True)
except NameError as e:
    print(e)
