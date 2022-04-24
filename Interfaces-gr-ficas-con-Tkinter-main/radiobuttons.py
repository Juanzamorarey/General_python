from tkinter import *
# Vamos a ver los botones radiales, se utilizan para seleccionar una opcion entre varias

def seleccionar():
    monitor.config(text="{}".format(opcion1.get()))
    # Con esta funcion configuramos la label de monitor para que muestre el texto de opcion1 el cual cambiará dependiendo del button seleccionado.
    # Nota: El metodo get() sirve para coger un valor, en este caso de opcion1 

def reset():
    opcion1.set(None)
    monitor.config(text="")
# Esta funcion reasigna el valor de opcion1 a None así como reiniciar el texto de monitor a un campo vacío.

root = Tk()

opcion1 = IntVar()



# # Todos los radiobuttons tienen un parametro que se asocia a una variable y un value, en este caso vamos a asignar la misma para los tres radiobuttons
# # COMENTAMOS PARA PODER SEGUIR CON LA LECCION
# Radiobutton(root, text="Opción 1",variable=opcion1,value=1).pack()
# Radiobutton(root, text="Opción 2",variable=opcion1,value=1).pack()
# Radiobutton(root, text="Opción 3",variable=opcion1,value=1).pack()
#Al asignar a todos el mismo valor nos permite seleccionar pero, al corresponder todos al mismo valor, no permite deseleccionar solo algunos, para ello debemos crear con diferentes values

Radiobutton(root, text="Opción 1",variable=opcion1,value=1,command=seleccionar).pack()
Radiobutton(root, text="Opción 2",variable=opcion1,value=2,command=seleccionar).pack()
Radiobutton(root, text="Opción 3",variable=opcion1,value=3,command=seleccionar).pack()
# Esto hace que, al corresponderse a una sola variable pero tener diferentes valores sean mutuamente excluyentes pudiendo seleccionar solo 1 opcion
# Vamos a crear una variable monitor que contenga una label la cual muestra por texto en la interfaz el valor de cada radiobutton mediante la funcion seleccionar, mas arriba

monitor = Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reset).pack()
# Creamos un boton que sirve para reiniciar el campo


root.mainloop()