"""
Dado un rango de números enteros, obtener la cantidad de números enteros que contiene.
"""
numeroInicial = int(input('Número Inicial: '))
numeroFinal = int(input('Número Final: '))
contador = 0

i = numeroInicial
while i <= numeroFinal:
    contador += 1
    i += 1

print(f'CANTIDAD: {contador}')
