import os
import csv
import pathlib

def registrar(nombre_archivo):
    '''Permite crear un archivo csv'''
    cantidad = int(input('cantidad: '))
    campos = ['Nombre', 'Fecha']    # llaves para el diccionario de writerow
    
    if not pathlib.Path(nombre_archivo).exists():
        with open(nombre_archivo, 'w', newline='', encoding='utf8') as archivo_csv:
            writer = csv.DictWriter(archivo_csv, fieldnames=campos)
            writer.writeheader()
    
    with open(nombre_archivo, 'a', newline='', encoding='utf8') as archivo_csv:
        writer = csv.DictWriter(archivo_csv, fieldnames=campos)
        for i in range(cantidad):
            nombre = input('Nombre: ')
            fecha = input('Fecha de nacimiento: ')
            writer.writerow({'Nombre': nombre, 'Fecha': fecha})


def leer(nombre_archivo):
    '''Permite leer el contenido del archivo csv'''
    with open(nombre_archivo, 'r', newline='', encoding='utf8') as archivo_csv:
        reader = csv.DictReader(archivo_csv)
        for i in reader:
            for campo, valor in i.items():
                print(f'{campo}: {valor}')

registrar('mi_archivo.csv')
leer('mi_archivo.csv')