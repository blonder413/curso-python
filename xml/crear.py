import xml.etree.cElementTree as ET

ruta = '/home/blonder413/Python/biblioteca-python/xml/'

root = ET.Element('root')

doc = ET.SubElement(root, 'doc')
ET.SubElement(doc, 'nodo1', name='nodo').text='texto nodo 1'
ET.SubElement(doc, 'nodo2', atributo='manzana').text='texto nodo 2'

doc = ET.SubElement(root, 'doc')
ET.SubElement(doc, 'nodo1', name='nodo').text='texto nodo 1 segundo doc'
ET.SubElement(doc, 'nodo2', atributo='manzana 2').text='texto nodo 2 segundo doc'

archivo = ET.ElementTree(root)
archivo.write(ruta + 'archivo_xml.xml') # Crea el archivo