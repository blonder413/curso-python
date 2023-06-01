import re

texto = "En este ejemplo de Python vemos cómo se manejan las expresiones regulares en python"
# match busca desde el principio de la cadena y es case sensitive
match = re.match("En este", texto)

# re.I = re.IGNORECASE -> no tiene en cuenta mayúsculas y minúsculas
match2 = re.match("en este", texto, re.IGNORECASE)
print(match2)
print(match2.span())

# search busca desde cualquier punto
search = re.search("en", texto, re.I)
print(search)

# devuelve una lista con el valor buscado
findall = re.findall("en", texto, re.I)
print(findall)

# devuelve una lista, separa cada elemento según el argumento pasado
split = re.split(" ", texto)
print(split)

# reemplaza el argumento pasado por otro, no reemplaza la cadena oficial
sub = re.sub("en", "EN", texto)
print(sub)
sub = re.sub("[P|p]ython", "PYTHON", texto)
print(sub)

# definir patrones personalizados, deben empezar por r
patron = r"[P|p]ython"
sub = re.sub(patron, "PYTHON", texto)
print(sub)
