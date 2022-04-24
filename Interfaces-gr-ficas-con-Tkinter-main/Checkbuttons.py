from tkinter import *

def seleccionar():
    cadena = ""
    if (leche.get()):#recordemos que leche y azucar tienen parametros 1=True y 0=False. Por esto si devuelve 1, o sea True, ocurre el if, sino ocurre el else que sería el 0
        cadena += "Con leche"
    else:
        cadena += "Sin leche"

    if (azucar.get()):
        cadena += " y con azúcar"
    else:
        cadena += " y sin azúcar"

    monitor.config(text=cadena) #Ahora le pasamos a monitor la cadena que hemos generado. OJO: SEGUIMOS DENTRO DE LA FUNCION

root = Tk()
root.title("Cafetería")
root.config(bd=15)
# Vamos a crear un botón de selección en el que el usuario elegirá como quiere que le sirvan el café.
# Estos botones dan únicamente la opción de seleccionar o no una opción

leche = IntVar() #1 si, 0 no
azucar = IntVar()

imagen= PhotoImage(file="cafe.gif")
Label(root, image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left") #Recuerda que el frame no se puede empacar directamente, es necesario separarlo en otra variable

Label (frame, text="¿Cómo quieres el café?").pack(anchor="w") #Con esta label asignamos una interfaz más ajustable al programa
# Los checkbuttones tienen dos parámetros muy importantes: onvalue(Qué ocurre si está marcado); y offvalue (qué ocurre si no está marcado))
# A estos parámetros se les aplica un valor de 1 (True) o 0 (False)
Checkbutton(frame, text="Con leche",variable=leche,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w") #Seleccionamos el Checkbutton al cual le incorporamos un text y le asignamos una variable
Checkbutton(frame, text="Con azúcar",variable=azucar,onvalue=1,offvalue=0,command=seleccionar).pack(anchor="w")#Con el command le asignamos la funcion de arriba

monitor = Label(frame) #Creamos una label para mostrar los valores que recuperemos de leche y de azucar 
monitor.pack()

root.mainloop()