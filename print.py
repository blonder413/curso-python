print("Este es un", end= " ")
print("ejemplo")

print("1","2","3","4","5")
print("1","2","3","4","5", sep=",")

nombre = "blonder"
numero = 413
print("el número es", numero)
print("el número es " + str(numero))

print("hola {} el número es {}".format(nombre, numero))
print("hola {nombre} el número es {numero}".format(numero=810, nombre="br"))
print("hola {1} el número es {0}".format(numero, nombre))

print("-hola %s, el número es %d" %(nombre, numero))
print("--hola %(nombre)s, el número es %(numero)d" %{'nombre':'blonder','numero':413})

# interpolación literal o f string
print(f'el número es {numero}')
print(f'el número es {numero + 1}')
print(nombre.center(50, '-'))
print(nombre.ljust(50, '-'))
print(nombre.rjust(50, '-'))
