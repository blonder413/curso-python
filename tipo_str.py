mensaje = 'hola' ' mundo'
print(f'id: {hex(id(mensaje))}')
mensaje += ' desde Python'
print(f'id: {hex(id(mensaje))}')    # se crea de nuevo la variable, toma otra dirección de memoria
mensaje = mensaje + ' concatenando cadenas'
mensaje.upper()    # Las cadenas son inmutables
print(mensaje)

texto = mensaje.upper()
print(texto)

nombre = ('jonathan', 'morales', 'salazar')
print('-'.join(nombre))
print(mensaje.split())

nombre = 'jonathan'
edad = 38
altura = 1.68
mensaje = 'nombre %s, edad %d años'%(nombre, edad)
mensaje = 'Nombre {} Edad {} EstAlturaatura {:.2f}'.format(nombre, edad, altura)
mensaje = 'Nombre {1} Edad {0} Altura {2:.2f}'.format(edad, nombre, altura)
mensaje = 'Nombre {n} Edad {e} Altura {a:.2f}'.format(e = edad, n = nombre, a = altura)
diccionario = {'nombre':'jonathan', 'edad':38,'altura':1.68}
mensaje = 'Nombre {persona[nombre]} - Edad {persona[edad]} - Altura {persona[altura]:.2f}'.format(persona=diccionario)
mensaje = f'Nombre {nombre} - Edad {edad} - Altura {altura}'
print(mensaje)

texto = 'Hola'*2
print(texto)

texto = 'hola mundoo\b' # \bborra el último caracter
texto = 'hola\nmundoo' # \n inserta un salto de línea
texto = r'No procesa los valores \n ni \b'  # raw string
texto = 'Hola\u0020Mundo\U0001F600'   # \u permite agregar un valor unicode, 4 valores para u y 8 valores para U
texto = 'Hola\x20Mundo'   # \x para hexadecimal
texto = 'Hol' + chr(97) +' Mundo'   # chr permite esribir caracteres ascii
print(texto)