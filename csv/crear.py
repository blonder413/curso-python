import csv
archivo = open("miarchivo.csv", "w+")
# writer = csv.writer(archivo)
writer = csv.writer(archivo, delimiter=';')
writer.writerow(['nombre', 'apellido', 'correo'])
writer.writerow(['jill', 'valentine', 'jvalentine@bsaa.org'])
archivo.close()
