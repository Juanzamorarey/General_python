from tkinter import *
# Vamos a meter las entry las cuales nos ayudan a que el usuario introduzca un valor
root = Tk()


# frame1 = Frame(root)
# frame1.pack()

# entry = Entry(frame1)
# # Creamos el metodo entry dentro del contenedor, en este caso root
# entry.pack(side="right")
# # Empacamos la variable en el programa


# label = Label(frame1, text="Nombre")
# label.pack(side="left")
# # Cuando creamos diferentes etiquetas el orden se hace muy caótico para solucionarlo podemos crear marcos que nos ayuden a separar los componentes de la interfaz
# # Para solucioarlo vamos a crear dos marcos e introducir en ellos los elementos que queremos meter:
# frame2 = Frame(root)
# frame2.pack()

# entry2 = Entry(frame2)
# entry2.pack(side="right")

# label2 = Label(frame2, text="Apellidos")
# label2.pack(side="left")

# Ahora los marcos nos han hecho de separadores, pero las labels no parecen estar bien alineadas lo que resta profesionalidad al programa, vamos a solcionar esto:
# Para ello vamos a reproducir esto en cuadricula con un metodo diferente a .pack() PD: PARA LLEVAR A CABO ESTA PARTE SE COMENTA EL CODIGO ANTERIOR



label = Label(root, text="Nombre")
label.grid(row=0,column=0,sticky="e",padx=5,pady=5)
# row es la fila y column es la columna
# Con el metodo .grid(rom, column,sticky) creamos una cuadricula a la que solamente tenemos que introducir la posicion dentro de dicha cuadricula
# Con el metodo sticky pegamos el texto a alguno de los lados siguiendo las indicaciones caridnales (e,w,n,s)
# También tenemos el metodo pad el cual sigue los ejes de coordenadas (x, y). En ambos ejes al introducir un valor introducimos una separacion en pixels que da mas formalidad

entry = Entry(root)
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify="center",state="normal")

label2 = Label(root, text="Apellidos")
label2.grid(row=1,column=0,sticky="e",padx=5,pady=5)

entry2 = Entry(root)
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify="center",state="normal",show="*")

# Las funciones de cambiar fuetne y colorear que hemos visto en la leccion anterior también están en los campos entry. Vamos a ver algunos mas:
# Por ejemplo al escribir en un campo el texto sale justificado a la izquierda. Eso es algo que podemos cambiar de la siguiente manera
# .config(justify="right"/"left"/"center")
# También podemos desactivar campos durante un momento, lo que podriamos hacer es lo siguiente
# .config(state="disabled"/"normal"), recordemos que esto se puede encadenar en un solo config. Esto hará que no se pueda clicar
# También podemos hacer que cuando se escribe en un campo se muestre algo diferente a lo que estamos escribiendo, por ejemplo cuando escribimos una contraseña
# .config(show="*")

root.mainloop()