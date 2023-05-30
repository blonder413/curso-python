"""
Un map genera un iterador operando cada valor de otro iterador
"""

numeros = [1, 2, 3, 4, 5]


def multiplicar(numero):
    return numero * 2


dobles = map(lambda n: n * 2, numeros)
print(list(dobles))

dobles = map(lambda n: n * 2, numeros)
print(list(dobles))
