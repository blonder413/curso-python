jill = ['jill', 'valentine']
claire = 'claire redfield'.split()

# print(jill + claire)  # No modifica las listas

jill.extend(claire)   # Agrega a la lista 1, los elementos de la lista 2
# print(jill)
jill.append('blonder')

# print(jill.index('morales'))    # obtener el índice del primer elemento que coincida
# jill.reverse()  # invierte el orden de la lista
# jill.sort() # ordena de forma ascendente
# jill = sorted(jill)
# jill.sort(reverse=True) # ordena de forma descendente
# jill = sorted(jill, reverse=True)
# jill = list(reversed(jill))
# jill.sort(key=len) # ordena por el tamaño de las listas o cantidad de caracteres
# print(jill)
# print(min(jill))    # mínimo
# print(max(jill))    # máximo

datos = jill.copy() # apuntan a diferentes direcciones de memoria
datos2 = jill   # apuntan a la misma dirección de memoria

print(jill)
