from tkinter import *

ventana = Tk()
ventana.geometry('600x600')

mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Nuevo archivo")
archivo.add_command(label="Nueva ventana")
archivo.add_separator()
archivo.add_command(label="Abrir archivo")
archivo.add_command(label="Abrir carpeta")
archivo.add_separator()
archivo.add_command(label="Salir", command=ventana.quit)

editar = Menu(mi_menu, tearoff=0)
editar.add_command(label="Nuevo archivo")
editar.add_command(label="Nueva ventana")
editar.add_separator()
editar.add_command(label="Abrir archivo")
editar.add_command(label="Abrir carpeta")
editar.add_separator()
editar.add_command(label="Salir", command=ventana.quit)

seleccion = Menu(mi_menu, tearoff=0)
seleccion.add_command(label="Nuevo archivo")
seleccion.add_command(label="Nueva ventana")
seleccion.add_separator()
seleccion.add_command(label="Abrir archivo")
seleccion.add_command(label="Abrir carpeta")
seleccion.add_separator()
seleccion.add_command(label="Salir", command=ventana.quit)

mi_menu.add_cascade(label='Archivo', menu=archivo)
mi_menu.add_cascade(label='Editar', menu=editar)
mi_menu.add_cascade(label='Seleccion', menu=seleccion)


ventana.mainloop()