# print(dir(__builtins__))    # Listado de funciones disponibles
numeros = [1, 2, 3]   # Puede sera una tupla
letras = ['a', 'b', 'c']
mezcla = zip(numeros, letras)    # Recibe valores iterables
# print(list(mezcla)) # se consuma una vez que se usa
print(tuple(mezcla))

# iterar en paralelo
for numero, letra in zip(numeros, letras):
    print(f'Numero: {numero}, letra: {letra}')

# separar un zip
mezcla = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*mezcla)

print(numeros, letras)

# ordenar
letras = ['j', 'b', 'y']
numeros = [8, 10, 4]
mezcla = zip(letras, numeros)

print(sorted(zip(letras, numeros)))

llaves = ['nombre', 'apellido']
valores = ['jill', 'valentine']
diccionario = dict(zip(llaves, valores))    # crear un diccionario
print(diccionario)

llave = ['nombre']
valor = ['claire']
diccionario.update(zip(llave, valor))   # Actualizar un valor de un diccionario
print(diccionario)
