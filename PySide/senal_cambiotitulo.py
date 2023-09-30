import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Boton
        self.boton = QPushButton('Clic aqui')
        # Asociamos la señal de clic al slot evento_clic
        self.boton.clicked.connect(self.evento_clic)
        # Conectar a la señal de cambio de titulo
        self.windowTitleChanged.connect(self.cambio_titulo_aplicacion)
        # Publicamos el boton
        self.setCentralWidget(self.boton)

    def evento_clic(self):
        # Cambiar el texto del boton y el titulo de la ventana
        self.boton.setText('Nuevo texto boton')
        self.boton.setEnabled(False)
        self.setWindowTitle('Nuevo Titulo de la Aplicacion')
        print('evento_clic')

    def cambio_titulo_aplicacion(self, nuevo_titulo):
        print(f'Nuevo titulo aplicacion: {nuevo_titulo}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
