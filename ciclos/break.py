"""
break rompe el ciclo, evita que se ejecute el else
"""
cont = 0
while(cont < 10):
    cont += 1
    if cont == 5:
        break
    print(cont)
else:
    print("fin del while")
