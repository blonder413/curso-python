'''
También conocido en otros lenguajes como maps, hashmaps, loookup tables
Las llaves deben ser inmutables
'''
from collections import OrderedDict

# diccionarios ordenados
ordenado = OrderedDict(uno=1, dos=2, tres=3)
ordenado['cuatro'] = 4
# print(ordenado)
print(ordenado.keys())
ordenado['dos'] = -2
# print(ordenado)
ordenado.pop('tres')
# print(ordenado)
ordenado['tres'] = 3
print(ordenado)
