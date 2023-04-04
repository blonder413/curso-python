'''
First class citizens: Las funciones son un objeto
'''
def sumar(a,b):
    return a + b

# asignar una función a una variable
mi_funcion = sumar
print(type(mi_funcion))
print(mi_funcion(4,5))

# función como argumentos
def operacion(a, b, sumar_arg):
    return sumar_arg(a,b)

print(operacion(4, 13, sumar))

# retornar función desde otras funciones
def retornar_funcion():
    return sumar    # regresamos la referencia de sumar()

retornada = retornar_funcion()
print(retornada(8,10))
