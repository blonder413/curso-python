'''
de lado derecho podemos definir una lista o tupla y se asigna a varias variables a la vez
'''

valores = 1,2,3
print(type(valores))

num1, num2, num3 = [1, 2, 3]
print(f'num1 = {num1}, num2 = {num2}, num3 = {num3}')

num1, _, num3 = 4, 13, 8  # el _ se usa para definir que es una variable que no se va a utilizar
print(num1, num3)

valor1, *valor2, valor3 = 1, 2, 3, 4 ,5
print(valor1, valor2, valor3)

def retorna_varios_datos():
    return 1, 2, 3  # En realidad regresa una tupla

print(type(retorna_varios_datos()))
num1, num2, num3 = retorna_varios_datos()
print(num1, num2, num3)

hora,_,minutos = '17:34'.partition(':')
print(hora, minutos)
