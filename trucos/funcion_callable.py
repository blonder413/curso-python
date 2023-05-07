'''
Todas las funciones en python son objetos
pero no todos los objetos son funciones
'''

def sumar(a, b):
    return a + b

suma = sumar(4, 13)
operacion = sumar

print(f'se puede llamar como función: {callable(suma)}')
print(f'se puede llamar como función: {callable(sumar)}')
print(f'se puede llamar como función: {callable(operacion)}')
print(f'se puede llamar como función: {callable("string")}')
