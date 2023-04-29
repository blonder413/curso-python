from PySide6.QtGui import QPalette, QColor
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.Window, QColor(color))
        self.setPalette(paleta)

class VentanaPrincipial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Layout en PySide')
        color = Color('yellow')
        self.setCentralWidget(color)

if __name__ == '__main__':
    app = QApplication()
    ventana = VentanaPrincipial()
    ventana.show()
    app.exec()
