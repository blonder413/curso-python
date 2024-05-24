"""
Manejo de fechas en Python
"""
from datetime import datetime, date, timedelta
import pytz

ahora = datetime.now()  # 2023-03-15 11:57:12.318996

anho = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

# formtear fechas
hoy = datetime.today()
FORMATO_DATE = '%Y-%m-%d'
FORMATO_DATETIME = '%Y-%m-%d %H:%M:%S'
print(hoy.strftime(FORMATO_DATETIME))

# convertir string en fecha
fecha = datetime.strptime('2023-03-15', FORMATO_DATE)

# operaciones weeks, days, hours, minutes, seconds, miliseconds, microseconds
fecha = date.today() # yyyy-mm-dd
print(f'ayer: {fecha - timedelta(days = 1)}')
print(f'día {datetime.weekday(fecha)}') # 0 - lunes

HOY = datetime.now(pytz.timezone("America/Santiago"))
FECHA = str(HOY.strftime(FORMATO_DATETIME))
print(FECHA)
