'''
higher order functions
Pasar funciones a otras funciones
'''
def llamar_funcion(funcion):
    return funcion()

def saludar():
    return 'Hola mundo'

def despedir():
    return 'Hasta luego'

print(llamar_funcion(saludar))
print(llamar_funcion(despedir))

def mayusculas(texto):
    return texto.upper()

# map recibe una función y lo aplica a cada uno de los argumentos del iterable
print(list(map(mayusculas, ['hola', 'bye'])))
print(list(map(mayusculas, 'hola blonder')))
