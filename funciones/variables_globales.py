contador = 0

def mostrar():
    print(contador)

def modificar(c):
    global contador
    contador = c

modificar(4)
mostrar()
