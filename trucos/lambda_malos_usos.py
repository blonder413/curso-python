'''
KISS: Keep It Simple Stupid
'''
class Prueba():
    mostrar = lambda self: print('hola mundo')

# No recomendado
lista_pares = list(filter(lambda i: i % 2 == 0, range(0,9)))
# Recomendado list comprehension
lista_pares = [i for i in range(0,9) if i % 2 == 0]
print(lista_pares)
