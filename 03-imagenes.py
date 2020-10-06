from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('700x500')

Label(ventana, text='Hola, soy Peyo').pack(anchor=W)

imagen = Image.open('./imagenes/perro.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()

ventana.mainloop()
