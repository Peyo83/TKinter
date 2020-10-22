"""
Crear:
- Ventana (Hecho)
- Tamaño fijo (Hecho)
- No redimensionable (hecho)
- Un menú (Inicio, Añadir, Info, Salir) (hecho)
- Opción de salir (hecho)
- Diferentes pantallas
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""

from tkinter import *

# Instanciar clase
ventana = Tk()

# Definir ventana
ventana.geometry('500x500')
ventana.title('Proyecto Tkinter')
ventana.resizable(0,0)

# Pantallas
def home():
    # Mostrar pantalla
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=20,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    # Mostrar pantalla
    add_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=20,
        pady=20
    )
    add_label.grid(row=0, column=0)

    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def info():
    # Mostrar pantalla
    info_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=20,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()

# Definir campos de pantallas
home_label = Label(ventana, text='Inicio')
add_label = Label(ventana, text='Añadir')
info_label = Label(ventana, text='Información')
data_label = Label(ventana, text='Creado por Juan Pedro Valladares - 2020')

# Cargar pantalla inicio
home()

# Menú superior
menu_superior = Menu(ventana)

inicio = Menu(menu_superior, tearoff=0)
inicio.add_command(label="Pantalla de inicio", command=home)

añadir = Menu(menu_superior, tearoff=0)
añadir.add_command(label="Pantalla de añadir", command=add)

informacion = Menu(menu_superior, tearoff=0)
informacion.add_command(label="Pantalla de información", command=info)

salir = Menu(menu_superior, tearoff=0)
salir.add_command(label="Salir", command=ventana.quit)

menu_superior.add_cascade(label='Inicio', menu=inicio)
menu_superior.add_cascade(label='Añadir', menu=añadir)
menu_superior.add_cascade(label='Información', menu=informacion)
menu_superior.add_cascade(label="Salir", menu=salir)

# Cargar menú
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()