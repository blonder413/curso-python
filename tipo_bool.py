'''
Para números: 0 es False, para cualquier otro valor es True
Para las cadenas, las cadenas vacías es False, para las demás es True
Para los diccionarios, los diccionarios vacíos es False, para los demás es True
Para las listas, las listas vacías es False, para las demás es True
Para las tuplas, las tuplas vacías es False, para las demás es True
'''
valor = bool(0)
valor = bool(413)
valor = bool('')
valor = bool({})
valor = bool([])
valor = bool( () )
print(valor)
