import pandas as pd
from pandas import ExcelWriter

ruta = '/home/blonder413/Python/biblioteca-python/excel/'
datos = pd.DataFrame({  # Datos que se van a pasar al excel
    'id': [1, 2, 3, 4],
    'nombre': ['jonathan', 'bridyith', 'cristian', 'sheina'],
    'apellido': ['morales', 'gonzález', 'castillo', 'montes']
})

datos = datos[['id', 'nombre', 'apellido']] # Formalizar los datos
writer = ExcelWriter(ruta + 'archivo.xlsx')
datos.to_excel(writer, 'Hoja 1', index=False)
writer.save()