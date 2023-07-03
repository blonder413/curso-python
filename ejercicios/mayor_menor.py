"""
ENUNCIADO: Ingrese 6 números en una lista y obtenga el número mayor y menor ingresado.

ANÁLISIS: Para la solución de este problema, se requiere que el usuario ingrese 6 números, luego el sistema devuelva el
número mayo y menor.
"""
numeros = []
for i in range(1,7):
    numeros.append(int(input(f"ingrese número {i}: ")))
print(numeros)
menor = min(numeros)
mayor = max(numeros)
print(f"menor: {menor} - mayor: {mayor}")
