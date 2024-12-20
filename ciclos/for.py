"""
El ciclo for permite ejecutar un bloque de código varias veces
el nombre de la variable asignada debe ser snake_case para cumplir la norma python:S117
"""
for value in range(10):
    print(value)

print('-'.rjust(10, '-'))

for value in range(1, 5):
    print(value)

print('-'.rjust(50, '-'))

for value in range(1,11):
    print(value)

print('-'.rjust(50, '-'))

for value in 'ethan':
    print(value)

print('-'.rjust(5, '-'))

for value in [1,2,3,4,5]:
    print(value)

print(''.rjust(50, '-'))

for value in (2,4,6,8):
    print(value)
