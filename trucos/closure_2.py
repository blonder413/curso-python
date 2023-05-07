def mostrar(titulo):
    def saludar(mensaje):
        return titulo + ' . ' + mensaje
    return saludar

mostrar_ing = mostrar('ingeniero')
mostrar_lic = mostrar('licenciado')

# ya posee la referencia de mostrar, así que podemos llamar a la función saludar
print(mostrar_ing('blonder'))
