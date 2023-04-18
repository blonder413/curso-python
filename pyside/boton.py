import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton
from PySide6.QtCore import QSize

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Botón')
        self.setFixedSize(800,600)
        boton = QPushButton('Nuevo Botón')
        self.setCentralWidget(boton)

if __name__ == '__main__':
    app = QApplication()
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())

