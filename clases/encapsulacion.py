class Persona:
    def __init__(self):
        self._nombre = 'jonathan'   # el _ indica que es protected
        self.__correo = 'blonder413@gmail.com'
    
    def get_correo(self):
        return self.__correo        # el __ indica que el atributo es privado
class Cliente(Persona):
    pass
class Helper():
    pass

persona = Persona()
# print(persona._nombre)
print(persona.__correo) # No puede llamar al atributo porque es privado
# print(persona.get_correo())

cliente = Cliente()
print(cliente._nombre)
# print(cliente.__correo) # No es posible llamarlo porque es privado
helper = Helper()
# print(helper._nombre) # no es posible llamado porque Helper no hereda de Persona
