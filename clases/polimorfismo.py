'''
En este módulo se muestra un ejemplo de polimorfismo
'''

class Persona:
    def saludar(self):
        return 'hola soy una persona'

class Cliente(Persona):
    pass

def get_nombre(persona: Persona):
    '''
    Como la clase cliente hereda de persona, 
    un objeto tipo cliente puede comportarse como una persona
    '''
    return persona.saludar()


cliente = Cliente()
print(get_nombre(cliente))
print(type(cliente))