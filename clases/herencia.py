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
    Permite acceder a los atributos y métodos protected y public de la clase padre
    '''

cliente = Cliente('jonathan')
print(cliente.publico())
print(cliente._protegido())
print(cliente.nombre)
# print(Persona().__privado())
print(Persona('jonathan').get_privado())
print(Persona('blonder413').nombre)
