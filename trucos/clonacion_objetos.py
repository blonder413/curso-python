# copia superficial (shallow o copia poco profunta)
lista_a = [[1,2], [3,4], [5,6]]
lista_b = list(lista_a) # dos objetos distintos
'''
aunque el objeto lista_b apunta a una dirección de memoria distinta de lista_a,
las listas internas apuntan a la misma dirección de memoria
'''
lista_a.append([7,8])
# son distintos objetos a nivel superior
print(lista_a)
print(lista_b)

lista_a[1][0] = 4
print(f'lista a: {lista_a}')
print(f'lista b: {lista_b}')
