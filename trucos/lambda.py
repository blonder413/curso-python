'''
permiten declarar funciones anónimas en una sola línea
no se puede utilizar decoradores ni agregar más de una línea de código
'''
def sumar(a,b):
    return a+b

suma = lambda a,b: a + b

print(suma(4,13))
print((lambda a,b: a + b)(4,13))
