from datetime import date
import hashlib
import os
from usuarios.conexion import conectar

database, cu = conectar()


class Usuario:
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password
        # salt = str(os.urandom(10)).encode('UTF-8')
        # self.password = hashlib.scrypt(password.encode('UTF-8'), salt=salt, n=2, r=8, p=1)

    def registrar(self) -> list:
        try:
            cifrado = hashlib.sha256()
            cifrado.update(self.password.encode('utf8'))

            fecha = date.today()
            sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
            usuarios = (self.nombre, self.apellido, self.email, cifrado.hexdigest(), fecha)  # para sha256
            # usuarios = (self.nombre, self.apellido, self.email, cifrado.hex(), fecha) # para scrypt
            cu.execute(sql, usuarios)
            database.commit()
            salt = str(os.urandom(10)).encode('UTF-8')
            cifrado2 = hashlib.scrypt(self.password.encode('UTF-8'), salt=salt, n=2, r=8, p=1)
            return [cu.rowcount, self]
        except Exception as e:
            print(e)
            return [0, self]

    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # usuario = (self.email, cifrado.hex())
        usuario = (self.email, cifrado.hexdigest())
        cu.execute(sql, usuario)
        return cu.fetchone()
