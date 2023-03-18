'''
No existe polimorfismo en Python
'''
class Persona:
    def saludar(self):
        return 'hola soy una persona'

class Cliente(Persona):
    pass

class Helper:
    pass

def get_nombre(persona: Persona):
    """
    Como la clase cliente hereda de persona, 
    un objeto tipo cliente puede comportarse como una persona
    """
    return persona.saludar()

cliente = Cliente()
print(get_nombre(cliente))

persona = Persona()
print(get_nombre(persona))

helper = Helper();
#print(get_nombre(helper))