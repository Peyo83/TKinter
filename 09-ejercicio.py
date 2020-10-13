'''
CALCULADORA:
- 2 campos de texto
- 4 botones
- Mostrar resultado en una alerta
'''

from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title('Ejercicio calculadora con Tkinter')
ventana.geometry('400x400')
ventana.config(bd=25)

def convertirFloat(numero):
    try:
        result = float(numero)
        return result
    except:
        messagebox.showerror("Error", "introduce bien los datos")

def sumar():
    resultado.set(convertirFloat(numero1.get()) + convertirFloat(numero2.get()))
    mostrarResultado()

def restar():
    resultado.set(convertirFloat(numero1.get()) - convertirFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(convertirFloat(numero1.get()) * convertirFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(convertirFloat(numero1.get()) / convertirFloat(numero2.get()))
    mostrarResultado()

def mostrarResultado():
    messagebox.showinfo('Resultado', f'El resultado de la operación es {resultado.get()}')
    numero1.set('')
    numero2.set('')

numero1 =StringVar()
numero2 =StringVar()
resultado =StringVar()

marco = Frame(ventana, width=350, height=200)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(anchor=CENTER)
marco.pack_propagate(FALSE) # Para que no se deforme al meter el formulario dentro

Label(marco, text='Primer número: ').pack()
Entry(marco, textvariable=numero1, justify='center').pack()

Label(marco, text='Segundo número: ').pack()
Entry(marco, textvariable=numero2, justify='center').pack()

Label(marco, text='') # Separador

Button(marco, text='Sumar', command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Restar', command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Multiplicar', command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Dividir', command=dividir).pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()