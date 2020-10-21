'''
CALCULADORA:
- 2 campos de texto
- 4 botones
- Mostrar resultado en una alerta
'''
from tkinter import *
from tkinter import messagebox

class Calculadora:

    def __init__(self, alertas):
        self.numero1=StringVar()
        self.numero2=StringVar()
        self.resultado=StringVar()
        self.alertas=alertas

    def convertirFloat(self, numero):
        try:
            result = float(numero)
            return result
        except:
            self.alertas.showerror("Error", "introduce bien los datos")

    def sumar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) + self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def restar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) - self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def multiplicar(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) * self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def dividir(self):
        self.resultado.set(self.convertirFloat(self.numero1.get()) / self.convertirFloat(self.numero2.get()))
        self.mostrarResultado()

    def mostrarResultado(self):
        self.alertas.showinfo('Resultado', f'El resultado de la operación es {self.resultado.get()}')
        self.numero1.set('')
        self.numero2.set('')


ventana = Tk()
ventana.title('Ejercicio calculadora con Tkinter')
ventana.geometry('400x400')
ventana.config(bd=25)

calculadora = Calculadora(messagebox)

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
Entry(marco, textvariable=calculadora.numero1, justify='center').pack()

Label(marco, text='Segundo número: ').pack()
Entry(marco, textvariable=calculadora.numero2, justify='center').pack()

Label(marco, text='') # Separador

Button(marco, text='Sumar', command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Restar', command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Multiplicar', command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text='Dividir', command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)



ventana.mainloop()