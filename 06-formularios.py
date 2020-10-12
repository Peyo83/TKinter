from tkinter import *

ventana = Tk()
ventana.geometry('700x400')
ventana.title("Formulario en Tkinter")

# Text Encabezado
encabezado = Label(ventana, text="Formulario utilizando Tkinter")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
# No se puede usar grid si se ha usadp pack, así que lo sustituyo
#encabezado.pack(side=LEFT, anchor=NW, fill = X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=2, sticky=W)

# Label para el campo (Nombre)
label = Label(ventana, text='Nombre')
label.grid(row=1, column=0, padx=5, pady=5)

# Campo de texto (Nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify='right', state='disabled')

# Label para el campo (Apellidos)
label = Label(ventana, text='Apellidos')
label.grid(row=2, column=0, padx=5, pady=5)

# Campo de texto (Apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify='left', state='normal')

# Label para el campo (Descripción)
label = Label(ventana, text='Descripción')
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

# Campo de texto (Apellidos)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30, 
    height=5,
    font=('Arial', 12),
    padx=15,
    pady=15
)

# Botón
Label(ventana).grid(row=4, column=1)
boton = Button(ventana, text='Enviar')
boton.grid(row=5, column=1, sticky=W)
boton.config(padx=10, pady=15, bg='green', fg='white')

ventana.mainloop()