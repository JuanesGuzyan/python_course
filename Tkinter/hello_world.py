# GUI - Graphical User Interface
# Tkinter - TK interface
# Importamos el modulo de tkinter
import tkinter as tk
# Importamos el modulo del tema de tkinter
from tkinter import ttk

# Creamos un objeto usando la clase tk
ventana = tk.Tk()
# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')
# Cambiamos el nombre de la ventana
ventana.title('Hello World')
# Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')


# Creamos un metodo evento_clic
def evento_clic():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento_clic')
    # Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()


# Crear un boton (widget - componente), el objeto padre es ventana
boton1 = ttk.Button(ventana, text='Dar Clic', command=evento_clic)
# Utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()
# Iniciamos la ventana (esta linea la ejecutamos al final)
# Si la ejecutamos antes, no se muestran los cambios anteriores
ventana.mainloop()
