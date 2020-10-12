from tkinter import *

ventana = Tk()
ventana.title('Ventana de Peyo')
ventana.geometry('700x700')

marco_padre = Frame(ventana, width=250, height=250)

marco_padre.pack(side=BOTTOM, fill=X, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='red',
    bd=5,
    relief=RAISED
)
marco.pack(side=LEFT, anchor=SW)
marco.pack_propagate(False)

texto = Label(marco, text='Primer marco')
texto.config(
    bg = 'red',
    fg = 'white',
    font=('Arial',20)
)
texto.pack(anchor=CENTER, fill=Y, expand=YES)

marco = Frame(marco_padre, width=250, height=250)
marco.config(
    bg='green',
    bd=5,
    relief=RAISED
)
marco.pack(side=RIGHT, anchor=SE)

marco_padre = Frame(ventana, width=250, height=250)

marco_padre.config(
    bg='lightblue',
    bd=5,
    relief=SOLID 
)

marco = Frame(marco_padre, width=250, height=250)

marco.config(
    bg='yellow',
    bd=5,
    relief=RAISED
)

marco.pack(side=LEFT, anchor=NW)

marco = Frame(marco_padre, width=250, height=250)

marco.config(
    bg='blue',
    bd=5,
    relief=RAISED
)

marco.pack(side=RIGHT, anchor=NE)

marco_padre.pack(side=TOP, fill=X, expand=YES)

ventana.mainloop()