class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f'Soy la persona. Nombre: {self.nombre}, apellido: {self.apellido}'

    def __repr__(self):
        """
        Está enfocado a dar información a los programadores
        Recomendado implementarlo si no vamos a implementar otro método
        """
        return f'{self.__class__.__name__}(nombre:{self.nombre}, apellido:{self.apellido})'

    def __format__(self, format_spec):
        return f'Mi clase es {self.__class__.__name__}, mis atributos son: {self.nombre} y  {self.apellido}'


persona = Persona('jill', 'valentine')
print(persona)  # por defecto llama al método __str__
print(f'{persona!r}')  # llamamos al método __repr__
print(f'{persona}')  # al usar el f en el print por defecto llama al método __format__
