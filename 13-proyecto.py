"""
Crear:
- Ventana (Hecho)
- Tamaño fijo (Hecho)
- No redimensionable (hecho)
- Un menú (Inicio, Añadir, Info, Salir) (hecho)
- Opción de salir (hecho)
- Diferentes pantallas (hecho)
- Formulario de añadir productos (hecho)
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
"""

from tkinter import *
from tkinter import ttk

# Instanciar clase
ventana = Tk()

# Definir ventana
#ventana.geometry('500x500')
ventana.minsize(500, 500)
ventana.title('Proyecto Tkinter')
ventana.resizable(0,0)

# Pantallas
def home():
    # Mostrar pantalla
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)
    products_box.grid(row=2)

    # Listar productos
    '''
    for product in products:
        if len(product) == 3:
            product.append('added')
            Label(products_box, text=product[0]).grid()
            Label(products_box, text=product[1]).grid()
            Label(products_box, text=product[2]).grid()
            Label(products_box, text='--------------').grid()
    '''
    for product in products:
        if len(product) == 3:
            product.append('added')
            products_box.insert('', 0, text=product[0], values = (product[1]))

    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()

def add():
    # Encabezado
    add_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=140,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)
    

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=('Consolas', 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=0, sticky=E)
    boton.config(
        padx = 15,
        pady = 5,
        bg = 'black',
        fg = 'white'
    )

    # Ocultar otras pantallas
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

def info():
    # Mostrar pantalla
    info_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=175,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # Ocultar otras pantallas
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

def add_products():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get('1.0', 'end-1c')
    ])
    name_data.set('')
    price_data.set('')
    add_description_entry.delete('1.0', 'end-1c')
    products_box.grid_remove()

    home()

# variables
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campo inicio
home_label = Label(ventana, text='Inicio')
#products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)
products_box = ttk.Treeview(heigh=12, columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text='Producto', anchor=W)
products_box.heading("#1", text='Precio', anchor=W)

# Definir campo añadir
add_label = Label(ventana, text='Añadir producto')

# Campos del formulario
add_frame = Frame(ventana) # Para no ir ocultando 1 a 1 los campos del formulario

add_name_label = Label(add_frame, text = 'Nombre: ')
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text = 'Precio: ')
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text='Descripción: ')
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text='Guardar', command=add_products)

# Definir campo información
info_label = Label(add_frame, text='Información')
data_label = Label(add_frame, text='Creado por Juan Pedro Valladares - 2020')

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