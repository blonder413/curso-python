import sys
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()
ventana = QPushButton('Botón de pyside')
# Cualquier componente puede ser una ventana
ventana.setWindowTitle('QPushButton')
ventana.resize(600,400)
ventana.show()
sys.exit(app.exec())
