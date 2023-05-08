'''
Los set son mutables
Los set manejan tipos de datos inmutables
Los set contienen valores únicos
'''
conjunto = {'Jonathan', 1.68, '1985-04-13', True}
set_vacio = set()
conjunto.add('blonder413@gmail.com')
conjunto.discard('jonathan')     # Elimina un elemento sin lanzar excepción
conjunto.remove('1985-04-13')    # Elimina un elemento, lanza excepción si no encuentra el elemento

conjunto = set([4,13,8,10])
conjunto2 = {1985,1986}
conjunto.update(conjunto2)
copia = conjunto2.copy()
print(id(copia), id(conjunto2))
print(conjunto2 is copia)

set1 = {1,2,3,4,5}
set2 = {0,2,4,6,8}
set3 = {1,3,5,7,9}
print(set2.union(set3))
print(set1.difference(set2))
print(set1.intersection(set2))
print(set1.symmetric_difference(set3))  # Todos menos los comunes (opuesto a intersection)
print(set1.issubset(set3))
print(set1.issuperset(set2))
print(set2.isdisjoint(set3)) # True si no tiene elementos comunes

# conjunto inmutable
a = frozenset({1,2,3})
# a.add(4) # no es posible agregar más elementos
