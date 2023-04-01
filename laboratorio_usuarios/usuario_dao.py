from cursor import Cursor
from logger_base import log
from usuario import Usuario

class UsuarioDao:
    '''
    Data Access Object tabla usuario
    '''
    __SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    __INSERTAR = 'INSERT INTO usuario (username, password) values (%s, %s)'
    __ACTUALIZAR = 'UPDATE usuario SET username = %s, password = %s WHERE id_usuario = %s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'

    @classmethod
    def seleccionar(cls):
        with Cursor() as cursor:
            log.debug(f'seleccionando usuarios')
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insertar(cls, usuario: Usuario):
        with Cursor() as cursor:
            log.debug(f'usuario a insertar: {usuario}')
            valores = (usuario.username, usuario.password)
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
    
    @classmethod
    def actualizar(cls, usuario : Usuario):
        with Cursor() as cursor:
            log.debug(f'Usuario a atualizar: {usuario}')
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
    
    @classmethod
    def eliminar(cls, usuario: Usuario):
        with Cursor() as cursor:
            log.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.id_usuario, )
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount

if __name__ == '__main__':
    usuarios = UsuarioDao.seleccionar()
    print(usuarios)
