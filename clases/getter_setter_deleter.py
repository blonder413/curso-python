class Persona:
    def __init__(self):
        self.__nombre = None
    
    @property   # Getter
    def nombre(self):
        return self.__nombre

    @nombre.setter  # Setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @nombre.deleter # Elimina el atributo de la instancia
    def nombre(self):
        del self.__nombre

persona = Persona()
persona.nombre = 'jonathan'
# del persona.nombre
print(persona.nombre)

