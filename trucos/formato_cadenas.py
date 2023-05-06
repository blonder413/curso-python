# estilo antiguo
nombre = 'blonder'
cadena = 'hola %s' % nombre
print(cadena)

error = 413
cadena = 'error en hexadecimal %x' % error  # %x hexadecimal
print(cadena)

cadena = 'hola %s error %i' % (nombre, error)
print(cadena)

cadena = 'hola %(n)s error %(e)i: %(e)x' % {'n':'blonder', 'e':error}
print(cadena)
