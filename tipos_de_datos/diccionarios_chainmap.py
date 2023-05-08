from collections import ChainMap

dic1 = {'uno': 1, 'dos':2, 'tres': 3}
dic2 = {'tres': -3, 'cuatro': 4, 'cinco': 5}
combinados = ChainMap(dic1, dic2)
print(combinados['tres'])
print(combinados['seis'])
