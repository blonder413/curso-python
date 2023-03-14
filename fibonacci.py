fin = int(input('ingrese el límite final: '))
numero_1, numero_2 = 0,1
while numero_2 < fin:
    print(numero_1, numero_2, end=" ")
    numero_1 += numero_2
    numero_2 += numero_1
print("")