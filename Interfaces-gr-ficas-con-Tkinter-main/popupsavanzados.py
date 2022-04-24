from tkinter import*
from tkinter import messagebox as MessageBox
# Las ventanas emergentes no están por defecto en tkinet por este motivo debemos importarlas. No es necesario renombrarlas pero lo hace el profe por el formato
from tkinter import colorchooser as ColorChooser
# Vamos a importar un set que nos permitirá hacer que el usuario pueda elegir entre diferentes colores
from tkinter import filedialog as FileDialog

root = Tk()

# def test():
    #MessageBox.showinfo("Hola","Esto es pa que veas lo que yo hago dura")
# El método showinfo() crea una ventana emergente que muestra información. Los argumentos tros son, por este oden: Título de la ventana y contenido de la ventana
    #MessageBox.showwarning("alerta", "regueton bien duro")
# El método showwarning() muestra una ventana emergente pero con caracter de alerta.
    # MessageBox.showerror("Error", "no llegaste suficiente abajo")
# Igual que el warning pero con caracter de error
#     resultado = MessageBox.askquestion("Salir","¿Estás seguro que quieres salir sin guardar?")
# Este .askquestion() devuelve un valor: una cadena de texto con la palabra "yes" o "no" a partir de la cual podemos continuar el programa. Por ejemplo:
#     if resultado =="yes":
#         root.destroy()#.destroy() rompe la ejecución del programa
# Ejecutando este programa aparecerá una ventana emergente diciendo si queremos cerrar. Si damos a sí saldremos del programa, si damos a no el programa continuará su ejecución.
    # resultado = MessageBox.askokcancel("Salir","¿Sobreescribir el fichero actual?")
# Este otro método devuelve en booleano: True, o False. Pero funciona de manera muy similar a .askquestion(). El método .askyesno() es igual pero devolviendo también true o false 
    # resultado = MessageBox.askyesno("Salir","¿Sobreescribir el fichero actual?")
    # if resultado:
    #     root.destroy()
    # resultado= MessageBox.askretrycancel("Reintentar","No se puede conectar")
# Esta dará una ventana emergente que tendrá dos opciones: reintentar la acción o cancelar la acción de maner automática. Devuleve un booleano como valor:
    # if resultado:
    #     root.destroy()

# A CONTINUACIÓN LAS POPUPS AVANZADAS
def test():
    # color= ColorChooser.askcolor(title="Elige un color")
    # print(color)
# Esto devuelve un valor, que no es otro que el color elegido en la paleta. El valor devuelto es una tupla con las coordenadas del color elegido en la paleta y 
# el código hexadecimal como segundo elemento lo que nos puede ayudar para, por ejemplo, referenciar dicho color en una página web
    # ruta= FileDialog.askopenfilename(title="Abrir un fichero", initialdir="C:", 
    # filetypes=(("Ficheros de texto","*.txt"),
    # ("Ficheros pdf","*.pdf"),
    # ("Todo tipo de fichero","*.*")) ) #Todo tipo de fichero
    # print(ruta)
# Este filedialog permite abrir un directorio hasta abrir un fichero y, en este caso, se guarda una cadena de caracteres la cual es la ruta al fichero
# Esto es vital puesto que a partir de este metodo y el get() podemos coger ficheros y trabajar con ellos. RECORDEMOS QUE DEVULEVE LA RUTA
# El segundo parámetro initialdir= indica desde dónde debe empezar la búsqueda, en este caso indicamos que desde el disco duro C:
# El tecer parámetro indica que tipo de ficheros se admiten en la búsqueda. dentro de filetypes(("nombre que asignamos a la búsqueda","*.formato"))
# Se trata por tanto de una tupla lo que introducimos en el metodo filetypes
# Es improtante resaltar que la tupla, oncluso cuando tiene un solo tipo de fichero requiere de una coma porque sino dará error. 
    fichero = FileDialog.asksaveasfile(title="Guardar un fichero",mode="w",defaultextension=".txt") #equivale a open ('ruta','w') La 'w' es el formato write por lo que se sobreescribe
    if fichero is not None:
        fichero.write("Hola")
        fichero.close()
# CUIDADO SI ABRIMOS UN FICHERO ASI NOS LO CARGAMOS; EL FORMATO 'W' LO DESTROZA
# Para evitar esto podriamos seleccionar otro modo: a -> append, w-> write (cuidado, por defecto), r-> read (no tiene sentido porque no se puede trabajar),r+ -> letura y escritura simultánea
# El parametro defaultextension es la extensión en la que saldrá el fichero al guardarlo.  
    print(fichero)
# Este método .asksaveasfile lo que muestra es una ruta donde podemos guardar un fichero.
# Cuando seleccionamos un fichero con este metodo lo sobreescribe y muestra por la terminal el fichero abierto en código con la propiedad name donde se encuentra la ruta de guardado
# File Dialog entonces abre un fichero y nos permite utilizarlo para guardar encima del propio fichero
# Atencion. Si en vez de seleccionar un fichero completamos el cmapo del nombre y damos a guardar crea automáticamente el fichero, pero debemos tener el modo 'w'

Button(root, text="Clícame",command=test).pack()


# Todas estas ventanas emergentes son únicamente de un tipo que muestra información y lleva a cabo una respuesta en algunos casos. 

root.mainloop()