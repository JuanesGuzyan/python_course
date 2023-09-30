from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel


class VentanaDialogo(QDialog):
    def __init__(self, padre=None):
        super().__init__(padre)
        self.setWindowTitle('Ventana de Dialogo')
        self.resize(300, 300)
        # Agregamos un boton de aceptar y cancelar
        botones = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.botones_dialogo = QDialogButtonBox(botones)
        self.botones_dialogo.accepted.connect(self.accept)
        self.botones_dialogo.rejected.connect(self.reject)
        # Definimos layout
        self.layout = QVBoxLayout()
        mensaje = QLabel('Presiona alguno de los botones')
        self.layout.addWidget(mensaje)
        self.layout.addWidget(self.botones_dialogo)
        self.setLayout(self.layout)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Dialogos')
        self.resize(500, 400)
        # Agregar un boton
        boton = QPushButton('Mostrar Dialogo')
        boton.clicked.connect(self.clic_boton)
        self.setCentralWidget(boton)

    def clic_boton(self, s):
        print(f'Clic sobre boton: {s}')
        dialogo = VentanaDialogo(self)
        valor_retornado = dialogo.exec()
        print(f'Valor retornado: {valor_retornado}')
        if valor_retornado:
            print('Se presiono Ok')
        else:
            print('Se presiono Cancel')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
