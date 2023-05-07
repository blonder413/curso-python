'''
Permite extender y modificar el comportamiento de una función, método o clase
es una función que recibe como parámetro otra función
ejemplos: logging, seguridad, caching
Es código reutilizable
'''
def decorador_envolvente(funcion_a_decorar):
    print('se ejecuta el decorador')
    return funcion_a_decorar

def saludar():
    print('hola mundo')

@decorador_envolvente
def saludar_decorada():
    return 'hola mundo desde decorada'

# forma manual, no es común
# funcion_retornada = decorador_envolvente(saludar)
# print(funcion_retornada)

print(saludar_decorada())