class Usuario:
    def __init__(self, id_usuario = None, username = None, password = None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
    
    def __str__(self):
        return f'Username: {self.__username} - Password: {self.__password}'
    @property
    def id_usuario(self):
        return self.__id_usuario
    @id_usuario.setter
    def id_usuario(slef, id_usuario):
        self.__id_usuario = id_usuario
    
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password
