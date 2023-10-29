"""
El operador := asigna y devuelve el contenido de la variable
"""
print(x := "Python")
print(type(x))


# Ejemplo sin walrus
# lista = []
# entrada = input("Escribe algo: ")
# while entrada != "terminar":
#     lista.append(entrada)
#     entrada = input("Escribe algo: ")

# print(lista)

# Ejemplo con walrus
lista = []
while (entrada := input("Escribe algo: ")) != "terminar":
    lista.append(entrada)

print(lista)
