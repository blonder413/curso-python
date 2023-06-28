"""
Dado un rango de números enteros num. inicial y num. final, obtener la cantidad de números positivos y negativos que
existen en el rango.
"""

n1 = int(input("límite menor: "))
n2 = int(input("límite mayor: "))
positivos = 0
negativos = 0

for n in range(n1, n2+1):
    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1
print(f"negativos: {negativos}. Positivos: {positivos}")
