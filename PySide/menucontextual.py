from PySide6.QtGui import QAction, QIcon, Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMenu


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu Contextual')
        # Mostramos y conectamos el menu contextual
        self.show()
        # Nos conectamos a la señal de CustomContextMenuRequested
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.contextMenuEvent)

    def contextMenuEvent(self, posicion):
        menu_contextual = QMenu(self)
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        boton_salir = QAction('Salir', self)
        # Conectamos a los triggers con la opcion de triggered
        boton_nuevo.triggered.connect(self.clic_boton_nuevo)
        boton_guardar.triggered.connect(self.clic_boton_guardar)
        boton_salir.triggered.connect(self.clic_boton_salir)
        menu_contextual.addAction(boton_nuevo)
        menu_contextual.addAction(boton_guardar)
        menu_contextual.addAction(boton_salir)
        # Recuperamos la posicion del cursor como posicion global de la ventana
        # y ejecutamos el menu contextual
        menu_contextual.exec(self.mapToGlobal(posicion))

    def clic_boton_nuevo(self, s):
        print('Opcion Nuevo...')

    def clic_boton_guardar(self, s):
        print('Opcion guardar')

    def clic_boton_salir(self, s):
        print('Opcion Salir')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
