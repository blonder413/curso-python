from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider

class ComponenteQSlider(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componente QSlider')
        self.__slider = QSlider(Qt.Horizontal)
        #self.__slider.setMinimum(4)
        #self.__slider.setMaximum(13)
        self.__slider.setRange(4,13)
        self.__slider.valueChanged.connect(self.__cambio_valor)
        self.__slider.sliderMoved.connect(self.__mueve_slider)
        self.__slider.sliderPressed.connect(self.__presiona_slider)
        self.__slider.sliderReleased.connect(self.__libera_slider)

        self.setCentralWidget(self.__slider)

    def __cambio_valor(self, valor):
        print(f'valor: {valor}')

    def __mueve_slider(self, valor):
        print(f'se movió el slider. El valor es: {valor}')

    def __presiona_slider(self):
        print('slider presionado')

    def __libera_slider(self):
        print('slider liberado')


if __name__ == '__main__':
    app = QApplication()
    ventana = ComponenteQSlider()
    ventana.show()
    app.exec()
