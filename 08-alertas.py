from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd=70)

def sacarAlerta():
    MessageBox.showinfo('Alerta', 'Hola, soy Peyo')

Button(ventana, text='Mostrar alerta!!!', command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion('Salir', 'H¿Quieres continuar ejecutando la aplicación?')

    if resultado != 'yes':
        MessageBox.showinfo('Chao!!', f'Adiós {nombre}')
        ventana.destroy()

Button(ventana, text='Salir', command=lambda: salir('Peyo')).pack()

ventana.mainloop()