#ELIAS MAMANI CALAMANI
from tkinter import*

#funciones de operaciones
def suma():
    total=int(entrada1.get())+int(entrada2.get())
    mensaje.set(total)

def resta():
    total = int(entrada1.get()) - int(entrada2.get())
    mensaje.set(total)

def multiplicacion():
    total = int(entrada1.get()) * int(entrada2.get())
    mensaje.set(total)

def division():
    total = int(entrada1.get()) / int(entrada2.get())
    mensaje.set(total)

def clear():
    mensaje.set('')
    num1.set('')
    num2.set('')

#UI
root=Tk()
root.geometry('250x305')
root.resizable(False,False)
root.title('CALCULADORA')
root.configure(bg="#FF5722")

num1=IntVar()
num2=IntVar()
mensaje = StringVar()

#Entradas de datos
entrada1=Entry(root,textvariable=num1,bg="#E64A19",fg="#FFFFFF",font=('', 15))
entrada1.pack()
entrada2=Entry(root,textvariable=num2,bg="#E64A19",fg="#FFFFFF",font=('', 15))
entrada2.pack()

#Botones de operadores
suma=Button(root, text="      suma      ",command=suma,bg="#FFC107",bd="0",fg="#FFFFFF",font=('', 15))
resta=Button(root,text="      resta      ",command=resta,bg="#FFC107",bd="0",fg="#FFFFFF",font=('', 15))
multiplicacion=Button(root,text="multiplicacion",command=multiplicacion,bg="#FFC107",bd="0",fg="#FFFFFF",font=('', 15))
division=Button(root,text="    division     ",command=division,bg="#FFC107",bd="0",fg="#FFFFFF",font=('', 15))

#mostrar resultado y limpiar pantalla
Label(root, textvariable=mensaje, bg="#FF5722",fg="#FFCCBC",font=('', 18)).place(x=25, y=230)
borrar=Button(root,text="CLEAR",command=clear,bg="#FFC107",bd="0",fg="#FFFFFF",font=('',10)).place(x=190, y=270)

suma.pack()
resta.pack()
multiplicacion.pack()
division.pack()

root.mainloop()