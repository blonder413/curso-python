import copy
lista_a = [[1,2], [3,4], [5,6]]
lista_b = copy.deepcopy(lista_a)    # distintos objetos a nivel superior

lista_a[1][0] = 4
print(f'lista a: {lista_a}')
print(f'lista b: {lista_b}')
