def imprimir_vector(x, y, z):
    print(f'<{x}, {y}, {z}>')

if __name__ == '__main__':
    imprimir_vector(4, 13, 0)
    tupla = (8,10,86)
    imprimir_vector(*tupla)
    lista = [4,13,8]
    imprimir_vector(*lista)

    generador = (x*x for x in range(3))
    imprimir_vector(*generador)

    diccionario = {'x': 4, 'y': 5, 'z': 6}
    imprimir_vector(**diccionario)
    # pasar las llaves
    imprimir_vector(*diccionario)
