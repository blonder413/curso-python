texto = b'cadena tipo byte'
print(texto[0]) # imprime el caracter asccii
print(chr(texto[0]))

texto = texto.decode('UTF-8')  # convertir bytes a string
print(texto)
texto = texto.encode('UTF-8') # convertir string a bytes
print(texto)