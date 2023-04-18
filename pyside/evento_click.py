from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y slots')
        boton = QPushButton('botón')
        boton.clicked.connect(self.__evento_click)
        self.setCentralWidget(boton)

    def __evento_click(self):
        print('hola blonder')

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
