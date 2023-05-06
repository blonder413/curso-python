'''
_ se usa para indicar que una variable es temporales o sin importancia
'''

for _ in range(3):
    print('hola')

valores = ['juan', 'perez', 13]
nombre, _, edad = valores
print(nombre)
print(edad)
