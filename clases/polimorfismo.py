"""
No es posible definir el tipo de parámetro de los métodos en Python
Para aprovechar el polimorfismo podemos usar la función isinstance(objeto, Clase)
"""
class Persona:
    def saludar(self):
        return 'hola soy una persona'

class Cliente(Persona):
    pass

class Helper:
    pass

def get_nombre(persona):
    """
    Como no existe la forma de pasar un tipo de parámetro a un método podemos validar usando la función isinstance()
    """
    if isinstance(persona, Persona):
        return persona.saludar()
    else:
        return 'Debe pasar una instancia de la clase Persona'
    #return persona.saludar()

cliente = Cliente()
print(get_nombre(cliente))

persona = Persona()
print(get_nombre(persona))

helper = Helper()
print(get_nombre(helper))
