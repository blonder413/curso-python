'''
las funciones son ciudadanos de primera clase
las funciones son objetos
'''
def mayusculas(texto):
    return texto.upper()

# uso normal, se debe definir o importar antes de llamarla
print(mayusculas('hola'))

# usar una función como un objeto
variable_funcion = mayusculas
print(mayusculas)
print(variable_funcion)
print(variable_funcion('hola'))

# eliminamos la referencia de la función
print(f'nombre por defecto de la función: {variable_funcion.__name__}')
del mayusculas
#print(mayusculas('hola'))
print(variable_funcion('hola'))

lista_funciones = [variable_funcion, str.upper]
print(lista_funciones)
for funcion in lista_funciones:
    print(funcion, funcion('hola blonder'))
print(lista_funciones[1]('hello blonder'))
