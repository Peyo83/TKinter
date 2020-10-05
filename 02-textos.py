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
texto.pack()

def pruebas(nombre, apellido, pais):
    return(f'Hola {nombre} {apellido}, veo que eres de {pais}')

texto = Label(ventana, text = pruebas(nombre=nombre, apellido=apellido, pais=pais))
texto.config(
    height=3,
    bg='orange',
    font=('Arial', 16),
    padx=10,
    pady=10,
    cursor='spider'
)
texto.pack(anchor=NE)


ventana.mainloop()