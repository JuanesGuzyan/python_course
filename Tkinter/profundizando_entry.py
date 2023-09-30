import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Entry')
ventana.iconbitmap('icono.ico')

# Definimos una variable que podremos modificar posteriormente (set), leer(get)
entrada_var1 = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)

# entrada1.insert(0, 'Introduce una cadena')
# entrada1.insert(tk.END, '.')


def enviar():
    # Recuperamos la informacion a partir de la variable asociada con la caja de texto
    # boton1.config(text=entrada_var1.get())
    # Modificacion utilizamos la variable de texto y el metodo set
    # entrada_var1.set('Cambio....')
    # Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())
    # Recuperamos la informacion
    # print(entrada_var1.get())
    # print(entrada1.get())


# Creamos un boton
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()
