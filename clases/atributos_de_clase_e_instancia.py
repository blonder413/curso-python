class Persona:
    edad = 0    # Atributo de clase

    def __init__(self, nombre, apellido):
        self.nombre = nombre    # atributo de instancia
        self.apellido = apellido    # atributo de instancia
persona1 = Persona('jonathan', 'morales')
print(persona1.__dict__)    # atributos del objeto

# creamos un atributo nuevo solo para este objeto
# al editar el valor no sobreescribimos el atributo de clase, creamos un atributo de objeto
persona1.edad = 38
print(persona1.edad)
print(persona1.__dict__)
print(Persona.edad) 
persona2 = Persona('bridyith', 'gonzález')
print(persona2.edad)
persona2.correo = 'bridyith@hotmail.com'
print(persona2.__dict__)

Persona.vivo = True # al crear objetos de clases se asocia a todos los objetos
print(persona2.vivo)
