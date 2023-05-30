'''
Una función que define otra función y la regresa
la función interna puede acceder a las variables de la función externa
'''


def operacion(a, b):
    def sumar():
        return a + b

    return sumar


print(operacion(4, 13)())


# Usando un lambda
def operacion(a, b):
    return lambda: a + b


print(operacion(8, 10)())


def sumar_valor():
    def agregar(valor):
        return valor + 4

    return agregar


closure_agregar = sumar_valor()(13)
print(closure_agregar)
