'''
En python no existe como en sí la sobrecarga de constructores
'''
class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None) # Llamamos al constructor

persona = Persona('jonathan', 'blonder413@gmail.com')
print(persona.nombre)
print(persona.correo)
persona_vacia = Persona.crear_persona_vacia()
print(persona_vacia.nombre)
