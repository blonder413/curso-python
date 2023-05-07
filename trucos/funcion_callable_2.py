'''
si queremos que una clase defina objetos que se pueden llamar como funciones
tenemos que sobreescribir el método __call__
'''
class Mostrar():
    def __init__(self, titulo):
        self.titulo = titulo
    
    def __call__(self, mensaje):
        '''
        Este método se llama cuando se usa un objeto como función
        '''
        return self.titulo + '. ' + mensaje

ing = Mostrar('inge')
print(ing('Blonder'))
print(f'Se puede llamar como función: {callable(ing)}')
