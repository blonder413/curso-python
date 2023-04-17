import sys
from PySide6.QtWidgets import QApplication, QMainWindow

class VentanaPySide():
    def __init__(self):
        self.ventana = QMainWindow()
        self.ventana.setWindowTitle('POO con PySide')
        self.ventana.resize(600,400)

if __name__ == '__main__':
    #app = QApplication(sys.argv)
    app = QApplication([])
    ventana1 = VentanaPySide()
    ventana1.ventana.show()
    app.exit(app.exec())