# Tkinter
# Módulo para crear interfaces gráficas de usuario

from tkinter import *
import os.path

class Programa:

    def __init__(self):
        self.title = 'Máster en Python'
        self.icon = './imagenes/imagen1.ico'
        self.icon_alt = './tkinter/imagenes/imagen1.ico'
        self.size = '770x470'
        self.resizable = False

    def cargar(self):
        # Crear la ventana raíz
        ventana = Tk()
        self.ventana = ventana

        # Título ventana
        ventana.title(self.title)

        # Comprobar si existe archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon)
        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)
        
        #Bloquear el tamaño de la ventana
        if self.resizable == True:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0) # Horizontal y verical. 0 bloquea 1 permite modificar

        # Arranar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()


# Instanciar programa
programa = Programa()
programa.cargar()
programa.addTexto('Ejemplo 1')
programa.addTexto('Ejemplo 2')
programa.mostrar()