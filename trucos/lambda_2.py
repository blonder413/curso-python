'''
podemos usar una función lambda siempre que necesitemos una función concreta
'''
lista_tuplas = [(1,'b'), (2,'f'), (5,'a'), (4,'c')]
lista_tuplas_ordenadas = sorted(lista_tuplas, key=lambda tupla: tupla[0])
lista_tuplas_ordenadas = sorted(lista_tuplas, key=lambda tupla: tupla[0], reverse=True)
print(lista_tuplas_ordenadas)

print(list(range(-3,4)))
for i in range(-3,4):
    print(i, i*i)

lista_ordenada = sorted(range(-3,4), key=lambda i: i*i)
print(lista_ordenada)

# closure con lambda
def mostrar(titulo):
    return lambda mensaje: titulo + '. ' + mensaje

mostrar_ing = mostrar('inge')
print(mostrar_ing('blonder'))
