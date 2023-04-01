from logger_base import log
from usuario import Usuario
from usuario_dao import UsuarioDao
import sys

opcion = None

while opcion != 5:
    print('Opciones:')
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Modifiar usuario')
    print('4. Eliminar usuario')
    print('5. Salir')
    opcion = int(input('Ingrese una opción: '))

    if opcion == 1:
        usuarios = UsuarioDao.seleccionar()
        for usuario in usuarios:
            # log.info(f'Username: {usuario.username}, password: {usuario.password}')
            log.info(usuario)
    elif opcion == 2:
        username = input('username: ')
        password = input('password: ')
        usuario = Usuario(username=username, password=password)
        usuarios_insertados = UsuarioDao.insertar(usuario)
        log.info(f'Usuarios insertados: {usuarios_insertados}')
    elif opcion == 3:
        id_usuario = int(input('id el usuario a modificar: '))
        username = input('Nuevo username: ')
        password = input('nuevo password: ')
        usuario = Usuario(id_usuario, username, password)
        usuarios_modificados = UsuarioDao.actualizar(usuario)
        log.info(f'Usuarios atualizados: {usuarios_modificados}')
    elif opcion == 4:
        id_usuario = int(input('ingrese el id del usuario a eliminar: '))
        usuario = Usuario(id_usuario=id_usuario)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        log.info(f'usuarios eliminadoos: {usuarios_eliminados}')
else:
    sys.exit()
