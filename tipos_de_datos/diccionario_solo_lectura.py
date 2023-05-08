from types import MappingProxyType

diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
diccionario['dos'] = -2
solo_lectura = MappingProxyType(diccionario)
# solo_lectura['tres'] = 4
print(solo_lectura)

# print(id(diccionario), id(solo_lectura))
