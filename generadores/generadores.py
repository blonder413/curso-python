'''
Permite regresar una secuencia de valores y suspende la ejecución hasta que se vuelva a llamar
no se usa return
útil cuando trabajamos con miles o millones de registros
'''
def generador():
    yield 1
    yield 2
    yield 3

valor = generador()
print(next(valor))
print(next(valor))
print(next(valor))

# Al intentar consumir más valores de los producidos se genera una excepción StopIteration

for valor in generador():
    print(valor)
