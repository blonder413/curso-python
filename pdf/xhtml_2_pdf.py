from xhtml2pdf import pisa
import os

ruta = '/home/blonder413/Python/biblioteca-python/pdf/'
nombre_archivo_html = 'xhtml_2_pdf.html'
sourceHtml = open(os.path.join(ruta, nombre_archivo_html)).read()    # Lee el HTML
outputFileName = ruta + 'xhtml_2_pdf.pdf'   # Nombre del archivo a generar

data = {'nombre': 'jonathan', 'ruta': ruta}

resultFile = open(outputFileName, 'w+b')    # Crea el PDF
pisaStatus = pisa.CreatePDF(sourceHtml, dest=resultFile)   # Guarda la información en el PDF

resultFile.close()  # Cerramos el archivo
