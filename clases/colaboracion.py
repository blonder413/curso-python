'''
Ejemplo de colaboración de objetos (inyección de dependencias)
'''

class Persona:
    '''
    Esta clase es la base para ser inyectada en otra
    '''
    def publico(self):
        '''
        Este método puede ser accedido desde cualquier clase
        '''
        return 'hola, soy la clase Persona'
class Cliente:
    def __init__(self):
        '''
        Definimos un atributo como instancia de otra clase (inyección de dependencia).
        Este atributo al ser una instancia debe llamarse usando punto (.). Ej: objeto.persona.atributo
        '''
        self.persona = Persona()

cliente = Cliente()
print(cliente.persona.publico())
