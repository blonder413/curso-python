"""
Las variables permiten dar un nombre a un espacio en memoria.
Así podemos acceder a los valores almacenados.
1. Puede contener letras mayúsculas y minúsculas, número y guión bajo(_)
2. No puede empezar con un número
3. No se pueden usar palabras reservadas cono for, if, class, etc
4. Es sensible a mayúsuclas y minúsculas
Se suele usar snake_case
Los nombres deben representar su contenido
"""

# El tipado es dinámico y no es estricto
edad = 28
altura = 1.68
# Definir el tipo de dato es solo para referencia, no lo hace estricto
pais: str = "Colombia"

print("edad:", edad)
print(f"altura: {altura}")
pais = 413
print(pais)

# Mostrar dirección de memoria
print(id(edad))

entero = 413
flotante = 1.68
nada = None
texto = "texto"
boleano = True  # Debe ir la primera letra en mayúscula (True/False)
