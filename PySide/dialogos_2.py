from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, \
    QMessageBox


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
        # Creamos el dialogo personalizada
        # dialogo = QMessageBox.question(self, 'Pregunta', 'Ventana con Pregunta')
        dialogo = QMessageBox.critical(self, 'Problema critico',
                                       'Ventana con Problema critico',
                                       buttons=QMessageBox.Discard | QMessageBox.NoToAll |
                                       QMessageBox.Ignore,
                                       defaultButton=QMessageBox.Discard)
        # Revisamos cual boton se presiona
        if dialogo == QMessageBox.Discard:
            print('Regreso el valor Discard')
        elif dialogo == QMessageBox.NoToAll:
            print('Regreso el valor de NoToAll')
        else:
            print('Regreso el valor de Ignorar')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
