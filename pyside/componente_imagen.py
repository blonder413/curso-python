from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap
import os

ruta_archivo = os.path.dirname(os.path.realpath('tkinter/logo.png'))
archivo = os.path.join(ruta_archivo, 'logo.png')
print(archivo)

class ComponenteImagen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente imagen')
        self.setFixedSize(400,400)
        etiqueta = QLabel('Nombre')
        etiqueta.setPixmap(QPixmap(archivo))
        etiqueta.setScaledContents(True)

        self.setCentralWidget(etiqueta)
        
if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteImagen()
    ventana.show()
    app.exec()
