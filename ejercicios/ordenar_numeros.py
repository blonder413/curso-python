"""
Dado 3 números, devolver los números en orden ascendente.
Para la solución de este problema, se requiere que el usuario ingrese tres números (n1, n2 y n3), luego el sistema
verifica y devuelve los números ordenados en forma ascendente.
Primero se debe encontrar el número Mayor, luego el número Menor y al final el número intermedio, que es el resultado
de la suma de los tres número - (Mayor + Menor).
"""
n1 = int(input("ingrese en número 1: "))
n2 = int(input("ingrese en número 2: "))
n3 = int(input("ingrese en número 3: "))

mayor = n1
menor = n1
intermedio = n1

if n1 > n2 and n1 > n3:
    mayor = n1
elif n2 > n1 and n2 > n3:
    mayor = n2
elif n3 > n1 and n3 > n2:
    mayor = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3

if n1 != mayor and n1 != menor:
    intermedio = n1
elif n2 != mayor and n2 != menor:
    intermedio = n2
elif n3 != mayor and n3 != menor:
    intermedio = n3

print(f"{menor} {intermedio} {mayor}")
