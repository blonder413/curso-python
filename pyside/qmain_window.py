import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication()
ventana = QMainWindow()
ventana.setWindowTitle('QMainWindow')
ventana.resize(600,400)
ventana.show()
sys.exit(app.exec())
