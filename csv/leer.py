import csv
with open("miarchivo.csv") as archivo:
    for linea in archivo.readlines():
        print(linea, end='')
