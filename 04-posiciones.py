from tkinter import *

nombre = input('Nombre: ')
apellido = input('Apellido: ')
pais = input('País: ')

ventana = Tk()
ventana.geometry('500x500')

texto = Label(ventana, text = 'Bienvenido a mi programa')
texto.config(
    fg='white',
    bg='black',
    padx=50,
    pady=20,
    font=('Consolas', 30)
    )
texto.pack(side=TOP)

def pruebas(nombre, apellido, pais):
    return(f'Hola {nombre} {apellido}, veo que eres de {pais}')

texto = Label(ventana, text = pruebas(nombre=nombre, apellido=apellido, pais=pais))
texto.config(
    height=3,
    bg='orange',
    font=('Arial', 18),
    padx=10,
    pady=20,
    cursor='spider'
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text = 'Básico 1')
texto.config(
    fg='white',
    bg='black',
    padx=10,
    pady=20,
    font=('Consolas', 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = 'Básico 2')
texto.config(
    fg='white',
    bg='orange',
    padx=10,
    pady=20,
    font=('Consolas', 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text = 'Básico 3')
texto.config(
    fg='white',
    bg='red',
    padx=10,
    pady=20,
    font=('Consolas', 30)
    )
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()