'''
defaultdict es una subclase de dict
'''
from collections import defaultdict
diccionario = defaultdict(lambda : 'Llave inexistente')
diccionario['a'] = 1
diccionario['b'] = 2
print(diccionario['c'])
diccionario_lista = defaultdict(list)
diccionario_lista['a'].append(1)
diccionario_lista['a'].append(2)
diccionario_lista['b'].append(3)
print(diccionario_lista)
