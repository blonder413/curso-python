numeros = [1,2,3]
print(*numeros)
print(*numeros, sep='-')

def sumar(a,b,c):
    print(f'Resultado de la suma: {a+b+c}')

numeros = [1,2,3]
sumar(*numeros)

lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [*lista1, *lista2] # junta los valores de ambas listas en una sola
print(lista3)

dic1 = {'A': 1, 'B': 2, 'C': 3}
dic2 = {'D': 4, 'E': 5}
dic3 = {**dic1, **dic2} # Para los diccinarios debe usarse doble *
print(dic3)

lista = [*'Nemesis']
print(lista)
