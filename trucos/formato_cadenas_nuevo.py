nombre = 'blonder'
cadena = 'hola {}'.format(nombre)
print(cadena)

error = 413
cadena = 'error {e:x}'.format(e=error)  # x = hexadecimal
cadena = 'error {e:.2f}'.format(e=error) # f = flotante
print(cadena)

# f string literal
cadena = f'hola {nombre} error {error:x}'
print(cadena)
print(f'resultado = {4 + 13:.2f}')
