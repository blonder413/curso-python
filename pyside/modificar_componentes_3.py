import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('componentes')
        self.setFixedSize(400,200)
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)
        contenedor = QWidget()
        contenedor.setLayout(disposicion)
        self.setCentralWidget(contenedor)

app = QApplication()
ventana = Ventana()
ventana.show()
sys.exit(app.exec())
