import sys
from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QSize

class VentanaPySide(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana con PySide')
        # self.resize(600, 400)
        self.setFixedSize(QSize(600,400))

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPySide()
    ventana.show()
    sys.exit(app.exec())
