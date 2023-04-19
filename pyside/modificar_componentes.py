'''
Modificar un componente por medio de slots
'''
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('modificar componentes')
        self.boton = QPushButton('click')
        self.boton.clicked.connect(self.__evento_click)
        self.setCentralWidget(self.boton)

    def __evento_click(self):
        self.boton.setText('Nuevo texto')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo título')

app = QApplication()
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
