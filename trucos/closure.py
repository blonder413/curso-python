'''
una función interna puede capturar y guardar el estado de la función externa
'''
def hablar(texto, volmen):
    def mayusculas(): 
        return texto.upper()
    def minusculas():
        return texto.lower()

    if volmen > 5:
        return mayusculas()
    else:
        return minusculas()

print(hablar('hola blonder', 6))
