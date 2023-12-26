from tkinter import *
import math

# inicializando la ventana:
raiz = Tk()
raiz.title("calculadora")
raiz.resizable(False,False)
 
main_frame = Frame(raiz )
main_frame.grid(row=0, column=0)

def ingresarValores(tecla):
    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")       
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
        
        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def ingresarValoresTeclado(event):
    tecla = event.char

    if tecla >= "0" and tecla <= "9" or tecla == "(" or tecla == ")" or tecla == ".":
        entrada2.set(entrada2.get() + tecla)

    if tecla == "*" or tecla == "/" or tecla == "+" or tecla == "-":
        if tecla == "*":
            entrada1.set(entrada2.get() + "*")
        elif tecla == "/":
            entrada1.set(entrada2.get() + "/")
        elif tecla == "+":
            entrada1.set(entrada2.get() + "+")       
        elif tecla == "-":
            entrada1.set(entrada2.get() + "-")
        
        entrada2.set("")

    if tecla == "=":
        entrada1.set(entrada1.get() + entrada2.get())
        resultado = eval(entrada1.get())
        entrada2.set(resultado)

def raizCuadrada():
    entrada1.set("")
    resultado = math.sqrt(float(entrada2.get()))
    entrada2.set(resultado)

def borrar(*args):
    inicio = 0
    final = len(entrada2.get())
    entrada2.set(entrada2.get()[inicio:final-1])

def borrartodo(*args):
    entrada1.set("")
    entrada2.set("")

# Declarando las barras de texto de la calculadora:
entrada1 = StringVar()
label1 = Label(main_frame, textvariable=entrada1, anchor = "e")
label1.grid(row=0, column=0, columnspan=4, sticky=(W, E))

entrada2 = StringVar()
label2 = Label(main_frame, textvariable=entrada2, anchor = "e")
label2.grid(row=1, column=0, columnspan=4, sticky=(W, E))

# definiendo los botones de los numeros:
boton0 = Button(main_frame, text="0", padx=40, pady=2, command = lambda: ingresarValores("0"))
boton1 = Button(main_frame, text="1", padx=15, pady=2, command = lambda: ingresarValores("1"))
boton2 = Button(main_frame, text="2", padx=15, pady=2, command = lambda: ingresarValores("2"))
boton3 = Button(main_frame, text="3", padx=16, pady=2, command = lambda: ingresarValores("3"))
boton4 = Button(main_frame, text="4", padx=15, pady=2, command = lambda: ingresarValores("4"))
boton5 = Button(main_frame, text="5", padx=15, pady=2, command = lambda: ingresarValores("5")) 
boton6 = Button(main_frame, text="6", padx=16, pady=2, command = lambda: ingresarValores("6"))
boton7 = Button(main_frame, text="7", padx=15, pady=2, command = lambda: ingresarValores("7"))
boton8 = Button(main_frame, text="8", padx=15, pady=2, command = lambda: ingresarValores("8"))
boton9 = Button(main_frame, text="9", padx=16, pady=2, command = lambda: ingresarValores("9"))

# definiendo los operadores:
boton_suma = Button(main_frame, text="+", padx=15, pady=2, command = lambda: ingresarValores("+"),bg="#DBDBDB")
boton_resta = Button(main_frame, text="-", padx=16, pady=2, command = lambda: ingresarValores("-"),bg="#DBDBDB")
boton_multiplicacion = Button(main_frame, text="*", padx=16, pady=2, command = lambda: ingresarValores("*"),bg="#DBDBDB")
boton_division = Button(main_frame, text=chr(247), padx=15, pady=2, command = lambda: ingresarValores("/"),bg="#DBDBDB")

# definiendo los operadores especiales:
boton_paretesis_inicial = Button(main_frame, text="(", padx=16, pady=2, command = lambda: ingresarValores("("),bg="#DBDBDB")
boton_paretesis_final = Button(main_frame, text=")", padx=16, pady=2, command = lambda: ingresarValores(")"),bg="#DBDBDB")
boton_borrar_todo = Button(main_frame, text="C", padx=15, pady=2, command = lambda: borrartodo(),bg="#DBDBDB")
boton_borrar = Button(main_frame, text=chr(9003), padx=12, pady=2, command = lambda: borrar(),bg="#DBDBDB")
boton_decimal = Button(main_frame, text=".", padx=18, pady=2, command = lambda: ingresarValores("."),bg="#DBDBDB")
boton_igual = Button(main_frame, text="=", padx=65, pady=2, command = lambda: ingresarValores("="),bg="#DBDBDB")
boton_raizcuadrada = Button(main_frame, text="√", padx=15, pady=2, command = lambda: raizCuadrada(),bg="#DBDBDB") 

# mostrando los botones en pantalla:
boton_paretesis_inicial.grid(row=2, column=0)
boton_paretesis_final.grid(row=2, column=1)
boton_borrar.grid(row=2, column=3)
boton_borrar_todo.grid(row=2, column=2)
boton7.grid(row=3, column=0)
boton8.grid(row=3, column=1)
boton9.grid(row=3, column=2)
boton_division.grid(row=3, column=3)
boton4.grid(row=4, column=0)
boton5.grid(row=4, column=1)
boton6.grid(row=4, column=2)
boton_multiplicacion.grid(row=4, column=3)
boton1.grid(row=5, column=0)
boton2.grid(row=5, column=1)
boton3.grid(row=5, column=2)
boton_suma.grid(row=5, column=3)
boton0.grid(row=6, column=0, columnspan=2)
boton_decimal.grid(row=6, column=2)
boton_resta.grid(row=6, column=3)
boton_igual.grid(row=7, column=0, columnspan=3)
boton_raizcuadrada.grid(row=7, column=3)


raiz.bind("<Key>",ingresarValoresTeclado)
raiz.bind("<KeyPress-b>",borrar)
raiz.bind("<KeyPress-v>",borrartodo)


raiz.mainloop()
