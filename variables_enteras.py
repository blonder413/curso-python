'''
int convierte un valor dado a entero decimal (no float)
'''

a = 10      # Decimal
b = 0b1010  # Binario
c = 0o12    # Octal
h = 0xA     # Hexadecimal

entero = int('23', 10)  # la base 10 es por defecto, se puede omitir
binario = int('10111', 2)   # binario a decimal
octal = int('27', 8)    # octal a decimal
hexadecimal = int('17', 16) # hexadeimal a decimal

print(binario)
