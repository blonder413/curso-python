jonathan = ['jonathan', 'morales', 'salazar']
bridyith = 'bridyith gonzález barragán'.split()

# print(jonathan + bridyith)  # No modifica las listas

jonathan.extend(bridyith)   # Agrega a la lista 1, los elementos de la lista 2
# print(jonathan)
jonathan.append('blonder')

# print(jonathan.index('morales'))    # obtener el índice del primer elemento que coincida
# jonathan.reverse()  # invierte el orden de la lista
# jonathan.sort() # ordena de forma ascendente
# jonathan = sorted(jonathan)
# jonathan.sort(reverse=True) # ordena de forma descendente
# jonathan = sorted(jonathan, reverse=True)
# jonathan = list(reversed(jonathan))
# jonathan.sort(key=len) # ordena por el tamaño de las listas o cantidad de caracteres
# print(jonathan)
# print(min(jonathan))    # mínimo
# print(max(jonathan))    # máximo

datos = jonathan.copy() # apuntan a diferentes direcciones de memoria
datos2 = jonathan   # apuntan a la misma dirección de memoria

print(jonathan)
