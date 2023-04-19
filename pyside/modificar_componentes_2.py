import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowTitleChanged.connect(self.__cambiar_titulo_ventana)
        self.setWindowTitle('Ventana')
        self.boton = QPushButton('click')
        self.boton.clicked.connect(self.__evento_click)
        
        self.setCentralWidget(self.boton)

    def __evento_click(self):
        self.setWindowTitle('Nueva ventana')

    def __cambiar_titulo_ventana(self):
        print('ha cambiado la ventana')
    
app = QApplication()    # debe ir antes de QMainWindow
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
