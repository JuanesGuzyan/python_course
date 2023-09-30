# POO con PySide
import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPyside(QMainWindow):
    def __init__(self):
        # Llamamos al metodo init de la clase Padre
        super().__init__()
        # self.ventana = QMainWindow()
        self.setWindowTitle('POO - PySide')
        # self.resize(600, 400)
        # Utilizamos setFixedSize(QSize())para colocar valores fijos
        self.setFixedSize(QSize(600, 400))
        # Creamos algunos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregar un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        # Agregamos algunas opciones al menu
        accion_nuevo = QAction('Nuevo', self)
        menu_archivo.addAction(accion_nuevo)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregar un mensaje en la barra de estado (inferior)
        self.statusBar().showMessage('Informacion de la barra de estado..')
        # Agregamos un boton
        boton = QPushButton('Nuevo boton')
        # Publicamos el boton en la ventana
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication([])
    # Creamos un objeto de tipo ventana
    ventana1 = VentanaPyside()
    ventana1.show()
    # Ejecutamos la ventana
    sys.exit(app.exec())
