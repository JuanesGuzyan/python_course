import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QDoubleSpinBox


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes - PySide')
        # QSpinBox es para valores numericos - int
        # numero = QSpinBox()
        # QDoubleSpinBox es para valores flotantes - float
        numero = QDoubleSpinBox()
        # Establecer valor minimo y maximo
        # numero.setMinimum(-5)
        # numero.setMaximum(8)
        numero.setRange(-5.5, 8.8)
        # Establecer prefijo y sufijo
        numero.setPrefix('$')
        numero.setSuffix('usd')
        # Establecemos el salto (step)
        numero.setSingleStep(3.5)
        # ValueChange(valor numerico), TextChange(se recibe prefijo, sufijo)
        # Envia el valor numerico
        numero.valueChanged.connect(self.cambio_valor)
        numero.textChanged.connect(self.cambio_texto)
        self.setCentralWidget(numero)

    def cambio_valor(self, nuevo_valor):
        print(f'Nuevo valor: {nuevo_valor}')

    def cambio_texto(self, nuevo_texto):
        print(f'Nuevo texto: {nuevo_texto}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
