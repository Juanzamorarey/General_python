from tkinter import * 
root = Tk()

# variable stringvar:
texto = StringVar()
# Asi nuestra stringar estaría vacia, conel metodo set le introducimos cosas
texto.set("Un nuevo texto")

root.title("Hola Mundo")
# root.iconbitmap('hqdefault.ico')
frame = Frame(root,width=480, height=320)
frame.pack()
# Label -> Etiqueta donde podemos mostrar algun texto estático

label = Label(frame, text="hola mundo frame")
# Creamos el objeto label que es un texto sencillo
# empaquetamos nuestro codigo para que aparezca. Cuidado porque da problemas con el tamaño. Para emplazar un widget utilizamos otro metodo: place(x=,y=) las coordenads x e y emplazan el widget
# label.place(x=100,y=100)
# Recordemos que hemos emplzado esta label dentro del marco, por lo que no se moverá fuera del mismo. Probemos a cambiar frame por root
label = Label(root, text="hola mundo root")
# # Como vemos en este caso si que no se mueve. Si no vamos a utilizar la variable podriamos aprovechar la sintaxis para crear varias etiquetas, una vez hecho esto podriamos moverlas
# Label(root, text="hola mundo root").pack(anchor="nw")
# # La anclamos al noroeste
# Label(root, text="otra etiqueta").pack(anchor="center")
# # Al centro
# Label(root, text="the final countdown").pack(anchor="se")
# # Al sureste

# Vamos a añadir algunas propiedades graficas a las Labels para lo que deberiamos tenerlas en una variable por lo que comentamos las anteriores y nos quedamos con la del centro
# Para recolocar la label que vamos a modificar debemos sacar afuera el pack a fin de evitar problemas:
label.pack(anchor="center")
label.config(bg="green",fg="blue",font=("calibri", 24))
# bg = cambio color de fondo, fg = cambio color letras, font =() cambio de tamaño, dos parametros (nombre de fuente, numero de tamaño)
# VAMOS A CREAR UNA VARIABLE QUE ADMITE CAMBIOS; PERO PARA HACERLO DEBEMOS HACERLO CERCA DE LA RAIZ POR LO QUE VA MAS ARRIBA OJOOOOOOO
label.config(textvariable=texto)
# MIRAR MAS ARRIBA ANTES DE CONTINUAR

# Tkinter admite también imagenes pero únicamente en formato gif y pgm

# imagen = PhotoImage(file="295196170_1.gif")
# Usamos el PhotoImage y en el atributo file le introducimos la ruta de la imagen, recordemos que debe estar en la misma carpeta
Label(root,image=imagen, bd=0).pack(side="left")
# Creada la imagen La introducimos en una label y la empaquetamos con el metodo .pack(). Para que funcione bien eliminar el frame. Se puede posicionar como cualquier widget



# Entry -> Entradas sencillas para escribir un texto corto

# text - > Campo de texto multilinea para textos largos

# Button -> Botón sobre el cual el usuario puede hacer click

# Radio Button -> Button radial para marcar una opcion

# Check button -> boton cuadrado que se puede marcar con un tick

# Menu -> estructura de botones centrados en lc omposicion de menus

# Boxes y dialogs -> Permiten mostrar mensajes al usuario 

root.mainloop()