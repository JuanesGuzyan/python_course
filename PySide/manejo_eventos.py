# Signals y Slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals y Slots')
        # Boton
        boton = QPushButton('Clic aqui')
        # Conectamos el evento checado (por default es False)
        boton.setCheckable(True)
        # Conectamos otro Slot al evento checkout
        boton.clicked.connect(self.evento_checar)
        # Conectamos el evento (Signal) Clic con el slot (evento_clic)
        boton.clicked.connect(self.evento_clic)
        # Publicamos el boton
        self.setCentralWidget(boton)

    def evento_checar(self, checar):
        self.boton_checado = checar
        print('Checado?', self.boton_checado)

    def evento_clic(self):
        print('Has hecho clic')
        # Accedemos al estado del boton (checado)
        print('Boton checado desde evento clic?', self.boton_checado)


if __name__ == '__main__':
    # Creamos el objeto aplicacion
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
