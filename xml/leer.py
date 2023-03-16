from xml.dom import minidom

ruta = '/home/blonder413/Python/biblioteca-python/xml/'

xml = minidom.parse(ruta + 'archivo_xml.xml')   # Leer el archivo

docs = xml.getElementsByTagName('doc')

for doc in docs:
    nodo1 = doc.getElementsByTagName('nodo1')[0]
    nodo2 = doc.getElementsByTagName('nodo2')[0]
    print(f'nodo1: {nodo1.firstChild.data}')
    print(f'nodo2: {nodo2.firstChild.data}')