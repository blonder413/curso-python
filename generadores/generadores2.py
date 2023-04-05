def generador():
    for numero in range(1,6):
        yield numero

valor = generador()
print(next(valor))
print(next(valor))

for valor in generador():
    print(valor)

generador = generador()
while True:
    try:
        valor = next(generador)
        print(valor)
    except StopIteration as e:
        break
