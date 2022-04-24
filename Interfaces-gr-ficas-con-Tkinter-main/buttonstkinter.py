from tkinter import*


# # SE COMENTAN ESTAS FUNCIONES PARA CREAR LAS DEL SUMATORIO:
# def hola():
#     print("hola")
# # Esta función la vamos a usar en el comportamiento del button. La funcion debe ponerse previa al botón

# def crear_label():
#     Label(root, text="Label creada dinámicamente").pack()
#     # Esta función crea una label con el texto asignado. Las funciones se pueden complicar escribiendo directamente el código que necesitamos



def sumar():
    r.set(float(n1.get())+float(n2.get())) #Con esta funcion ejecutamos la suma
    borrar()
def restar():
    r.set(float(n1.get())-float(n2.get())) #Con esta funcion ejecutamos la suma
    borrar()
def dividir():
    r.set(float(n1.get())/float(n2.get())) #Con esta funcion ejecutamos la suma
    borrar()
def multiplicar():
    r.set(float(n1.get())*float(n2.get())) #Con esta funcion ejecutamos la suma
    borrar()

# Vamos a crear una funcion que elimina los números de los campos de suma una vez ejecutada la operación
def borrar():
    n1.set("")
    n2.set("")

root= Tk()
root.config(bd=15)
root.resizable(0,0)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

# entero = IntVar()  # Declara variable de tipo entera
# flotante = DoubleVar()  # Declara variable de tipo flotante
# cadena = StringVar()  # Declara variable de tipo cadena
# booleano = BooleanVar()  # Declara variable de tipo booleana


Label(root,text="Número 1").pack(side="left")
entry1 = Entry(root,justify="left",textvariable=n1).pack(side="left") #primer numero
Label(root,text="Número 2").pack(side="left")
entry2 = Entry(root,justify="left",textvariable=n2).pack(side="left") #segundo numero
Label(root,text="Resultado").pack(side="left")
Label(root,text="").pack(side="left") #Esta label da un espacio previo a la suma de modo que queda mas ordenada la interfaz
resultado = Entry(root,justify="left",textvariable=r,state="disabled").pack(side="left") #resultado. El estado disabled hace que no se pueda modificar el resultado


# Las modificaciones esteticas son libres en este punto. Cabe destacar que podriamos usar los \n para establecer saltos de linea entre unos resultados y otros


frame = Frame(root,width=80,height=80).pack(side = "right", anchor="n")

Button(frame, text="Sumar", command=sumar).pack(side="right",anchor="n")
Button(frame, text="Restar", command=restar).pack(side="right",anchor="n")
Button(frame, text="Multiplicar", command=multiplicar).pack(side="right",anchor="n")
Button(frame, text="Dividir", command=dividir).pack(side="right",anchor="n")



# Creamos un boton con un texto y lo empacamos directamente en el contenedor root. Para añadir un comportamiento debemos añadir command al botón y asignarle una función:
# TODAS LAS FUNCIONES VAMOS A COLOCARLAS PREVIAS A LA ROOT DE LA INTERFAZ.
# Con esto podremos ver los cambios en la terminal, pero no en la interfaz. Para ello vamos a crear una función que cree una label




root.mainloop()