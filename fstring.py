"""
el f string es una forma de formatear texto
"""
import datetime

VALOR = 13.04
# Definimos la cantidad de decimales
decimal = f"{VALOR:.5f}"
print(VALOR, decimal)

VALOR = 1304
# Reemplazamos el separador de miles por un punto
neto = f"${VALOR:,}".replace(',','.')
print(VALOR, neto)

FECHA = datetime.datetime(2023, 7, 12, 16, 13, 58)
fecha_formateada = f"{FECHA:%d-%m-%Y}"
print(FECHA, '-', fecha_formateada)
