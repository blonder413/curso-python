multiplicacion = (valor * valor for valor in range(4))
print(multiplicacion)
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

suma = sum(valor * valor for valor in range(4))
print(suma)

lista = ['ethan', 'winters']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

lista = ['rose', 'winters']
contador = 0
def incrementar():
    global contador
    contador += 1
    return contador
generador = (f'{incrementar()} . {nombre}' for nombre in lista)
lista2 = list(generador)
print(lista2)
cadena = ', '.join(lista2)
print(cadena)
