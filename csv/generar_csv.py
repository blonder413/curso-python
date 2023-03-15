import csv

# importante que el archivo no se llame csv o interferirá con la importación del módulo

def registrar(nombre_archivo):
    cantidad = int(input('cantidad a registrar: '))
    with open(nombre_archivo, 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=',')
        for i in range(cantidad):
            titulo = input('Titulo: ')
            anho = input('Año: ')
            writer.writerow([titulo, anho])

def leer(nombre_archivo):
    with open(nombre_archivo, 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for linea in reader:
            print(f'Título: {linea[0]}')
            print(f'Año: {linea[1]}')

# registrar('nombre_archivo.csv')
leer('nombre_archivo.csv')