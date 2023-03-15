from datetime import datetime, date, time, timedelta

ahora = datetime.now()  # 2023-03-15 11:57:12.318996

anho = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

# formtear fechas
hoy = datetime.today()
formato_date = '%Y-%m-%d'
formato_datetime = '%Y-%m-%d %H:%M:%S'
print(hoy.strftime(formato_date))

# convertir string en fecha
fecha = datetime.strptime('2023-03-15', formato_date)

# operaciones weeks, days, hours, minutes, seconds, miliseconds, microseconds
fecha = date.today() # yyyy-mm-dd
print(f'ayer: {fecha - timedelta(days = 1)}')
print(f'día {datetime.weekday(fecha)}') # 0 - lunes