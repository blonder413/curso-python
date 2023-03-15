from xhtml2pdf import pisa
import os
from jinja2 import Template

ruta = '/home/blonder413/Python/biblioteca-python/pdf/'
nombre_archivo_html = 'jinja_pdf.html'
sourceHtml = open(os.path.join(ruta, nombre_archivo_html)).read()    # Lee el HTML
outputFileName = ruta + 'jinja.pdf'   # Nombre del archivo a generar

data = {'nombre': 'jonathan', 'ruta': ruta}

resultFile = open(outputFileName, 'w+b')    # Crea el PDF

template = Template( open(os.path.join(ruta, nombre_archivo_html)).read() ) # Leemos el archivo HTML
html = template.render(data)    # Pasamos información al HTML
pisaStatus = pisa.CreatePDF(html, dest=resultFile)  # Guarda la información en el PDF

resultFile.close()  # Cerramos el archivo
