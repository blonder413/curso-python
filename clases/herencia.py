'''
Ejemplo de herencia
'''

class Persona:
    '''
    Este clase brinda métodos y atributos a las clases que la hereden
    '''
    def __init__(self, nombre):
        '''
        En las instancias de la clase Persona y las que hereden deben recibir el nombre como parámetro
        '''
        self.nombre = nombre
    def publico(self):
        '''
        Este método puede ser accedido desde cualquier clase
        '''
        return 'hola, soy la clase Persona'
    def __privado(self):
        '''
        este método solo puede ser accedido desde la misma clase
        '''
        return 'hola, soy un método privado'
    def _protegido(self):
        '''
        Este método puede ser accedido desde la clases que hereden
        '''
        return 'hola, soy un método protegido'
    def get_privado(self):
        return self.__privado()

class Cliente(Persona):
    '''
    Se debe indicar el nombre de la clase padre entre paréntesis
    Permite acceder a los atributos y métodos protected y public de las clases padre
    Python permite herencia múltiple, se deben separar las clases padre por coma.
    En caso de la herencia múltiple con métodos iguales se llamará a la clase nombrada primero en el paréntesis
    No es necesario sobreescribir el constructor si no voy a recibir más parámetros
    '''

cliente = Cliente('Mia')
print(cliente.publico())
print(cliente._protegido())
print(cliente.nombre)
# print(Persona().__privado())
print(Persona('mia').get_privado())
print(Persona('ethan').nombre)
