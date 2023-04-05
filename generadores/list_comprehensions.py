numeros = range(10)
lista_pares = []
for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero * numero)
# print(lista_pares)

# List comprehensions
# [expresion for variable in coleccion if condición]
lista_pares = []
# lista_pares = [numero * numero for numero in numeros]
lista_pares = [numero * numero for numero in numeros if numero % 2 == 0]
# print(lista_pares)

pares = [numero for numero in range(50) if numero % 4 == 0 if numero % 6 == 0]
# print(pares)

lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
#print(lista_pares, lista_impares)

lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero % 2 == 0 else lista_impares.append(numero) for numero in range(10)]
# print(lista_pares, lista_impares)

lista = [[1,2,3], [4,5,6], [7,8,9]]
lista_simple = [valor for sublista in lista for valor in sublista]
#print(lista_simple)

# ------------------------------------------------------------------------

lista_pares = []
for sublista in lista:
    for valor in sublista:
        if valor % 2 == 0:
            lista_pares.append(valor)

lista_pares = [valor for sublista in lista for valor in sublista if valor % 2 == 0]

print(lista_pares)
