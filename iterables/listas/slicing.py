"""
Slicing hace referencia a tomar una parte específica de las listas en lugar de
la lista completa
"""
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(lista[0])     # muesta el primer valor
print(lista[-1])    # muestra el último valor
print(lista[1:])    # muestra desde el índice indicado hasta el final
print(lista[:3])    # muestra desde el cero hasta el índice indicado -1
print(lista[::2])   # salta de a 2
print(lista[0:8:2])   # se pueden combinar el índice inicial, final y salto
print(len(lista))   # largo de la lista
