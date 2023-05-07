def hablar(volumen):
    def minusculas(texto):
        return texto.lower()
    def mayusculas(texto):
        return texto.upper()
    if volumen > 5:
        return mayusculas
    else:
        return minusculas
    
print(hablar(6)('hola blonder'))

minusculas = hablar(5)
print(minusculas('hola Blonder'))
