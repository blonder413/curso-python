class Persona:
    def __init__(self):
        self.__nombre = None

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    def __str__(self):  # Se llama automáticamente al imprimir el objeto
        return f'mi nombre es {self.nombre}'

juan = Persona()
juan.nombre = 'jonathan'
print(juan)