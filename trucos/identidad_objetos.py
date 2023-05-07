'''
diferencias entre == y el operador is en POO
== compara el contenido de dos objetos que pueden apuntar a dos objetos
distintos
is verifica que ambos objetos apunten a la misma direción de memoria
'''
lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]
lista_d = list(lista_a)

print(lista_a == lista_b)
print(lista_a is lista_b)
print(lista_a == lista_c)

# regresa False porque aunque tengan el mismo contenido apuntan a diferentes
# direcciones de memoria
print(lista_a is lista_c)
print(lista_d is lista_a)   # apunta a una dirección de memoria distinta
