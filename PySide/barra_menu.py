from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QApplication, \
    QLabel, QToolBar, QStatusBar, QCheckBox


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Barra De Herramientas')
        self.resize(500, 400)
        # Publicamos una etiqueta
        etiqueta = QLabel('Hello')
        etiqueta.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(etiqueta)

        # Creamos la barra de herramientas
        barra = QToolBar('Barra de Herramientas')
        barra.setIconSize(QSize(16, 16))
        barra.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        # Configuracion para mostrar la barra de herramientas (lin 19)
        # barra.setToolButtonStyle(Qt.ToolButtonTextOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonIconOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextBesideOnly)
        # barra.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addToolBar(barra)

        # Creamos el boton para la barra
        boton_nuevo = QAction(QIcon('nuevo.png'), 'Nuevo', self)
        # Agregamos el boton a la barra
        barra.addAction(boton_nuevo)

        # Barra de estado
        self.setStatusBar(QStatusBar(self))

        # Mostramos mensaje del boton accion
        boton_nuevo.setStatusTip('Nuevo archivo')

        # Mostrar Slot - asociar evento clic
        boton_nuevo.triggered.connect(self.clic_boton_nuevo)

        # Hacemos checable el boton
        # boton_nuevo.setCheckable(True)

        # Agregamos la opcion de guardar archivo
        boton_guardar = QAction(QIcon('guardar.png'), 'Guardar', self)
        barra.addAction(boton_guardar)
        boton_guardar.setStatusTip('Guardar')
        boton_guardar.triggered.connect(self.clic_boton_guardar)

        barra.addSeparator()

        barra.addWidget(QCheckBox())
        barra.addWidget(QLabel('Salir'))

        menu = self.menuBar()
        menu_archivo = menu.addMenu('&Archivo')
        menu_archivo.addAction(boton_nuevo)

        # Agregamos una segunda opcion
        menu_archivo.addAction(boton_guardar)

        # Agregamos un separador
        menu_archivo.addSeparator()

        # Agregamos una tercera opcion
        boton_salir = QAction('Salir', self)
        menu_archivo.addAction(boton_salir)

        # Submenu ayuda
        boton_acerca_de = QAction(QIcon('acerca.png'), 'Acerca De', self)
        menu_ayuda = menu.addMenu('Ayuda')
        menu_ayuda.addAction(boton_acerca_de)

        # Agregamos slot a boton Acerca De
        boton_acerca_de.triggered.connect(self.clic_boton_acerca)

        # Submenu del menu de archivo
        menu_archivo.addMenu(menu_ayuda)

        # Ej. Combinacion de teclas
        # Creacion de atajos
        # boton_nuevo.setShortcut(QKeySequence('Ctrl+n'))
        # Manera similar cualquier sistema operativo
        boton_nuevo.setShortcut(Qt.CTRL | Qt.Key_N)
        # Atajo acerca de - Ctrl + 1
        boton_acerca_de.setShortcut(Qt.CTRL | Qt.Key_1)
        # Atajo Guardar - CTRl + G
        boton_guardar.setShortcut(Qt.CTRL | Qt.Key_G)

    def clic_boton_acerca(self, s):
        print(f'Acerca de....{s}')

    def clic_boton_nuevo(self, s):
        print(f'Nuevo archivo: {s}')

    def clic_boton_guardar(self, s):
        print(f'Guardando archivo..: {s}')


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
