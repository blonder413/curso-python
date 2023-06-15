"""
Crea un archivo excel por cada hoja del excel dado
pip install pandas
pip install openpyxl
"""
import pandas as pd
from pandas import ExcelWriter
from datetime import datetime
from conectar import getDato, setDatos

sql = f"select * from fillrate where estado_id = 4;"
dato = getDato(sql)

if dato is not None:
    archivo = dato[2]
else:
    archivo = ""

ruta = "/var/www/html/public/uploads/fillrate/"
hoy = datetime.today()
formato = "%m%d%Y"
fecha = hoy.strftime(formato)


def crear_excel_hoja_0(archivo: str) -> None:
    """
    Crear el archivo con la primer hoja del excel
    Parameters
    ----------
    archivo : str
        Nombre del archivo a leer
    """
    try:
        hoja = pd.read_excel(ruta + archivo, engine='openpyxl')
        hoja[['% Dispo']] = hoja[['% Dispo']].astype('float64')
        hoja[['% Dispo']] = hoja[['% Dispo']].applymap(lambda n: f"{n * 100:.2f}")
        hoja[['% Dispo']] = hoja[['% Dispo']].astype('str')
        hoja[['% Dispo']] = "=\"" + hoja[['% Dispo']] + "\""

        hoja = hoja[[
            'Periodo', 'Nombre', 'Rut Proveedor', 'Lin. Ped', 'Lin. Rec',
            '% Dispo', '    Monto Pedido', '  Monto Recibido', '   Monto Pérdida',
            '%Perdida  $'
        ]]  # Formalizar los datos
        archivo = dato[2].replace('fillrate_', 'HFRRE00')
        writer = ExcelWriter(ruta + archivo)
        hoja.to_excel(writer, "Hoja 1", index=False)
        writer.close()
        print(f"creado excel {archivo}")
    except Exception as e:
        print(e)


def crear_excel_hoja_1(archivo: str) -> None:
    """
    Crear el archivo con la segunda hoja del excel
    Parameters
    ----------
    archivo : str
        Nombre del archivo a leer
    """
    hoja = pd.read_excel(ruta + archivo, sheet_name="Detalle x Sección", engine='openpyxl')
    hoja[['% Disp']] = hoja[['% Disp']].astype('float64')
    hoja[['% Disp']] = hoja[['% Disp']].applymap(lambda n: f"{n * 100:.2f}")
    hoja[['% Disp']] = hoja[['% Disp']].astype('str')
    hoja[['% Disp']] = "=\"" + hoja[['% Disp']] + "\""

    hoja = hoja[[
        'Periodo', 'Nombre', 'Rut Proveedor', 'Lin. Ped', 'Lin. Rec',
        '% Disp', '    Monto Pedido', '  Monto Recibido', '   Monto Pérdida',
        '%Perdida  $', 'Sección'
    ]]  # Formalizar los datos
    archivo = dato[2].replace('fillrate_', 'HFRSE00')
    writer = ExcelWriter(ruta + archivo)
    hoja.to_excel(writer, "Hoja 1", index=False)
    writer.close()
    print(f"creado excel {archivo}")


def crear_excel_hoja_2(archivo: str) -> None:
    """
    Crear el archivo con la tercer hoja del excel
    Parameters
    ----------
    archivo : str
        Nombre del archivo a leer
    """
    hoja = pd.read_excel(ruta + archivo, sheet_name="Detalle x OC", engine='openpyxl')
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].astype('float64')
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].applymap(lambda n: f"{n * 100:.2f}")
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].astype('str')
    hoja[['%Disponible Q']] = "=\"" + hoja[['%Disponible Q']] + "\""

    hoja = hoja[[
        'Periodo', '  Nombre', 'Rut Proveedor', 'N° OC', 'Canal Entrega',
        'Sección', 'Lin. Ped', 'Lin. Rec', '%Disponible Q', '    Monto Pedido',
        '  Monto Recibido', '   Monto Pérdida', '%Perdida  $'
    ]]  # Formalizar los datos
    archivo = dato[2].replace('fillrate_', 'HFROC00')
    writer = ExcelWriter(ruta + archivo)
    hoja.to_excel(writer, "Hoja 1", index=False)
    writer.close()
    print(f"creado excel {archivo}")


def crear_excel_hoja_3(archivo: str) -> None:
    """
    Crear el archivo con la cuarta hoja del excel
    Parameters
    ----------
    archivo : str
        Nombre del archivo a leer
    """
    hoja = pd.read_excel(ruta + archivo, sheet_name="Detalle x Sku", engine='openpyxl')
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].astype('float64')
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].applymap(lambda n: f"{n * 100:.2f}")
    hoja[['%Disponible Q']] = hoja[['%Disponible Q']].astype('str')
    hoja[['%Disponible Q']] = "=\"" + hoja[['%Disponible Q']] + "\""

    hoja = hoja[[
        'Periodo', '  Nombre', 'Rut Proveedor', 'Sku', 'Descripción ', 'Sección',
        'Lin. Ped', 'Lin. Rec', '%Disponible Q', '    Monto Pedido',
        '  Monto Recibido', '   Monto Pérdida', '%Perdida  $'
    ]]  # Formalizar los datos
    archivo = dato[2].replace('fillrate_', 'HFRSK00')
    writer = ExcelWriter(ruta + archivo)
    hoja.to_excel(writer, "Hoja 1", index=False)
    writer.close()
    print(f"creado excel {archivo}")


if dato is not None:
    setDatos(f"update fillrate set estado_id=88 where id='{dato[0]}';")
    crear_excel_hoja_0(archivo)
    crear_excel_hoja_1(archivo)
    crear_excel_hoja_2(archivo)
    crear_excel_hoja_3(archivo)
    setDatos(f"update fillrate set estado_id=25 where id='{dato[0]}';")
