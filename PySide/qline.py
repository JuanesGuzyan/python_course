import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit


class Componentes(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Componentes - PySide')
        # Componente QLineEdit
        linea_texto = QLineEdit()
        # Max de caracteres
        linea_texto.setMaxLength(15)
        # Establecemos un texto de ayuda
        linea_texto.setPlaceholderText('Introduce tu nombre:')
        # Solo lectura
        # linea_texto.setReadOnly(True)
        # Validacion (Mask)
        linea_texto.setInputMask('00-0000-0000')
        # Evento enter, cambio seleccion texto, cambio texto
        linea_texto.returnPressed.connect(self.enter_presionado)
        linea_texto.selectionChanged.connect(self.cambio_seleccion)
        linea_texto.textChanged.connect(self.cambio_texto)
        self.setCentralWidget(linea_texto)

    def enter_presionado(self):
        print('Se presiono el enter')
        self.centralWidget().setText('00-0000-0000')

    def cambio_seleccion(self):
        print('Cambio seleccion texto')
        print(self.centralWidget().selectedText())

    def cambio_texto(self, nuevo_texto):
        print('Cambio de texto')
        print(nuevo_texto)


if __name__ == '__main__':
    app = QApplication([])
    ventana = Componentes()
    ventana.show()
    sys.exit(app.exec())
