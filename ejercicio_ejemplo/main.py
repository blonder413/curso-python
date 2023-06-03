"""
Proyecto Python/MSQL
- abrir asistente
- registro de usuario
- inicio de sesión
- crear, mostrar y borrar notas
"""

from usuarios.acciones import Acciones

print('''
Acciones disponibles:
    - Registro
    - Login
''')

acciones = Acciones()
accion = input('Ingrese la opción: ')

if accion.lower() == 'registro':
    acciones.registro()
elif accion.lower() == 'login':
    acciones.login()
else:
    print('opción incorrecta')
