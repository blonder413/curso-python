numeros = [1,2,2,8,5,4,6,4,9]

for i in numeros:
    print(i)

print('pop'.rjust(10, '-'))

numeros.pop()
numeros.pop(2)

for i in numeros:
    print(i)

print('remove'.rjust(10, '-'))
numeros.remove(4)

for i in numeros:
    print(i)

print('del'.rjust(10, '-'))
del numeros[0:2]

for i in numeros:
    print(i)

numeros.clear() # Elimina todos los elementos de la lista
print(numeros)

del numeros # Elimina la variable
print(numeros)  # Genera error porque la lista ya no existe
