try:
    archivo = open('prueba.txt', 'w', encoding='utf8')   # Creamos el archivo para escritura
    archivo.write('agregamos información al archivo')
    archivo.write('\nagregamos otra línea')
except Exception as e:
    print(e)
#finally:
    #archivo.close()
