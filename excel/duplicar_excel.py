"""
pip install pandas
pip install openpyxl
"""
import pandas as pd

ruta = "/home/blonder413/public_html/easygoproject/public/uploads/fillrate/"
archivo = "fillrate_2023_06_12_11_06_26.xlsx"

df = pd.read_excel(ruta + archivo)
df.to_csv(ruta + "data_export.csv", index=False)
df.to_excel("data_export.xlsx", sheet_name="Sheet1")
