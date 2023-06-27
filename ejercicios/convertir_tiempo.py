"""
Crear un programa que permita convertir una cantidad de segundos en horas, minutos y segundos.
"""
tiempoSegundos = input('Tiempo en Segundos: ')
HORA = 3600
MINUTO = 60

tiempoSegundos = int(tiempoSegundos)

h = tiempoSegundos // HORA
tiempoSegundos = tiempoSegundos % HORA
m = tiempoSegundos // MINUTO
s = tiempoSegundos % MINUTO

print('Horas:', h, '- Minutos:', m, '- Segundos:', s)
