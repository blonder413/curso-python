'''
PySide es la implementación gratuita de Qt
'''
import sys
from PySide6.QtWidgets import QApplication, QWidget

# Clase base de Qt (PySide)
# solo debe existir una instancia de QApplication
app = QApplication()
ventana = QWidget()
ventana.setWindowTitle('Pyside')
ventana.resize(600,400)
ventana.show()
sys.exit(app.exec())
