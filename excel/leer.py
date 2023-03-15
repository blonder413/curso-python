import xlrd

ruta = '/home/blonder413/Python/biblioteca-python/excel/'
documento = xlrd.open_workbook(ruta + 'archivo.xls')    # Abrir el archivo

datos = documento.sheet_by_index(0) # Leer la primera hoja

for i in range(datos.nrows):
    if i > 0:
        print(f'Id: {repr( int(datos.cell_value(i, 0)) )} | Nombre: {repr(datos.cell_value(i, 1))}')