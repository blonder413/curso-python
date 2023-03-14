NOMBRE = " Jonathan "
APELLIDO = "Morales"

# elimina los espacios al principio y al final
print(NOMBRE.strip() + APELLIDO) 
print(NOMBRE + APELLIDO.strip("M"))
print(NOMBRE + APELLIDO.strip("s"))
# busca la J, al no encontrarla busca el espacio
# al encontrarlo vuelve a buscar la J
print(NOMBRE.strip("J "))

print(NOMBRE.rstrip() + APELLIDO)
print(NOMBRE.lstrip() + APELLIDO)