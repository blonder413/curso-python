# son mutables

numeros = [1,2,2,2,5,4,4,3]
print(type(numeros))
numeros[2] = 3
numeros[4] = 5
numeros.append(6)

print('numeros'.rjust(1, '-'))
for i in numeros:
    print(i)

print('-'.rjust(10, '-'))

lista = ['blonder', 413]
lista.insert(1, 'br')
for i in lista:
    print(i)

print('-'.rjust(10, '-'))
print(lista[0])
print(len(lista))

print('extend'.rjust(10, '-'))
lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8]
lista1.extend(lista2)
print(lista1)

print('suma'.rjust(10, '-'))
print(f'{sum(lista2)}')