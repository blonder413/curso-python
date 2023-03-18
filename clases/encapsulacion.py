class Persona:
    def __init__(self):
        self._nombre = 'jonathan'   # el _ indica que es protected
        self.__correo = 'blonder413@gmail.com'
    
    def get_correo(self):
        return self.__correo        # el __ indica que el atributo es privado

persona = Persona()
print(persona._nombre)
print(persona.get_correo())