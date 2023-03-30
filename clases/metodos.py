'''
Los métodos estáticos se relacionan con la clase en sí misma
'''

class Metodos:
    variable_de_clase = 'Variable de clase'

    def __init__(self):
        self.variable_de_instancia = 'Variable de instancia'

    @staticmethod
    def metodo_statico():
        '''
        No pueden acceder a los atributos de instancia ya que la clase se carga antes de instanciarse
        '''
        return Metodos.variable_de_clase
    
    @classmethod
    def metodo_de_clase(cls):
        '''
        Puede ser accedido desde una instancia o llamando a la clase sin instanciarla
        Recibe un parámetro de clase de la instancia en sí misma
        Se recomiendo nombrarlo cls pero se puede usar cualquier nombre
        No puede acceder a métodos o variables de instancia
        '''
        return cls.variable_de_clase    # Usamos el parámetro cls para llamar los atributos de clase

print(Metodos.metodo_statico())
print(Metodos.metodo_de_clase())
