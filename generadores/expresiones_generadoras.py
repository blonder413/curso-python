multiplicacion = (valor * valor for valor in range(4))
print(multiplicacion)
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))
print(next(multiplicacion))

suma = sum(valor * valor for valor in range(4))
print(suma)

lista = ['jonathan', 'morales']
generador = (valor for valor in lista)
print(next(generador))
print(next(generador))

lista = ['bridyith', 'gonzález']
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
