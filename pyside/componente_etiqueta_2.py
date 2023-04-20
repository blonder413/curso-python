from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QLabel, QApplication

class ComponenteEtiqueta2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente etiqueta')
        etiqueta = QLabel('Hola')
        etiqueta.setText('Hello')
        fuente = etiqueta.font()
        fuente.setPointSize(18)
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteEtiqueta2()
    ventana.show()
    app.exec()
