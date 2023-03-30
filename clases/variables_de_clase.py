'''
Los atributos de clases son como atributos estáticos, todas las instancias tienen el mismo valor
'''
class VariablesDeClase:
    '''
    Las variables de clase pueden ser accedidas sin instanciar un objeto
    También puede ser accedida desde cualquier instancia
    '''
    variable_de_clase = 'Todas las instancias tienen el mismo valor'

    def __init__(self, valor):
        '''
        Las variables de instancia solo pueden ser accedidas desde una instancia
        '''
        variable_de_instancia = valor   # Cada instancia tendrá su propio valor

# VariablesDeClase.variable_de_clase = 'modificado'

VariablesDeClase.nueva_variable_de_clase = 'nuevo atributo'

print(VariablesDeClase.variable_de_clase)
print(VariablesDeClase.nueva_variable_de_clase)
