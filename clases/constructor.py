class Persona:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

persona = Persona('jonathan', 'blonder413@gmail.com')
print(persona.nombre)
print(persona.correo)
