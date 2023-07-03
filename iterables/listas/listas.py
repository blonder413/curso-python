"""
son mutables
puede almacenar distintos tipos de datos
Se recomienda un espacio en blanco entre cada elemento
"""
numeros = [1, 2, 2, 2, 5, 4, 4, 3]
print(type(numeros))
numeros[2] = 3
numeros[4] = 5
numeros.append(6)

print('numeros'.rjust(1, '-'))
for i in numeros:
    print(i)

print('insert'.rjust(10, '-'))

lista = ['blonder', 413]
lista.insert(1, 'br')   # se inserta en el índice indicado, los valores después se corren a la derecha
for i in lista:
    print(f'{lista.index(i)}: {i}')

print('extend'.rjust(10, '-'))
lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8]
lista1.extend(lista2)   # los datos de lista2 se ponen al final de lista1
print(lista1)
