'''
nos conectamos a la base de datos
'''
# pip install mysql-connector-python
import mysql.connector

try:
    config = {
        'host' : 'localhost',
        'port' : 3306,
        'user' : 'blonder413',
        'passwd' : 'Mono/1985',
        'database' : 'blonder413'
    }
    database = mysql.connector.connect(**config)
except Exception as e:
    print(e)

try:
    cu = database.cursor(buffered = True)
except NameError as e:
    print(e)