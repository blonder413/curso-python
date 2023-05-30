"""
Filter permite filtrar sobre un iterable
"""


def filtrar_mayores(valor):
    if valor > 10:
        return True
    else:
        return False


numeros = [4, 13, 5, 10, 19]
filtrados = filter(filtrar_mayores, numeros)
print(list(filtrados))
filtrados = filter(lambda n: n < 10, numeros)
print(list(filtrados))
