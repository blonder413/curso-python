numero_1 = int(input('Ingrese el número 1: '))
numero_2 = int(input('Ingrese el número 2: '))

if numero_1 > numero_2:
    print(f'{numero_1} es mayor que {numero_2}')
elif numero_2 > numero_1:
    print(f'{numero_2} es mayor que {numero_1}')
else:
    print('Son iguales')

if numero_1 > numero_2 or \
        numero_2 > numero_1:
    print('son distintos')
