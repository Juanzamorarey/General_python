# Tkinter es un módulo con componentes gráficos llamados widgets a partir de los cuales podemos construir las interfaces gráficas del programa.

# Estos widgets tienen una jerarquida interna que estructura la interfaz, en este curso veremos los siguientes:

# TK -> contenedor de todos los widgets que forman la interfaz. 

from tkinter import * 
# De esta manera importamos todo tkinter
root = Tk()
# Una vez creada la raíz debemos introducir el bucle del programa que lo ejecutará hasta que elijamos una opción que termine el bucle

root.title("Hola Mundo")
# Establece el titulo de la ventana
root.resizable(1,1)
# Esto hace que la ventana no sea redimensionable. Los parámetros 0 y 1 indican posible o no posible aquí. La primera posicion es lo vertical, la segunda horizontal
root.iconbitmap('hqdefault.ico')
# Si en esta funcion introducimos una imagen .ico (solo funciona este formato) este será el formato de nuestro programa
# Si al guardar el programa cambiamos la terminacion a pyw no aparecerá una terminal de fondo cuando abramos la interfaz por lo que queda mucho mas limpio, pero no se podrá ver lo que 
# ocurre como en la terminal de visual code
# root.mainloop()
# El mainloop es el bucle principal para el programa. DEBE IR SIEMPRE ABAJO DEL TODO AQUI SE DEJA POR MOTIVOS PEDAGÓGICOS

# Frame -> Marco, puede tener tamaño propio o posicionarse en lugares de otro contenedor
frame = Frame(root,width=480, height=320)
# Creamos una variable Frame que contiene un marco (FRAME()) el cual a su vez en el argumento debe llevar su contenedor, en este caso root. También podemos meter aqui las medidas
# frame.pack()
# De esta manera frame se distribuye en sí mismo. Cuidado porque por defecto no tiene ningun tamaño y la ventana desaparecería
# frame.config(width=480, height=320)
# Con config asignamos un tamaño además de otros estandar. width (anchura), height(altura). También se pueden poner en el Frame
# El metodo pack alinea los widgets arriba y al medio frame.pack(). Si lo queremos de otra forma lo cambiamos como aqui abajo
frame.pack(side="right",anchor="n")
# Dependiendo de la alineacion que asignemos el marco se alineará en un lugar u otro primer parametro side=(right, bottom, left, top) para los lados. 
# Segundo paramatro anchor = (north(n),west(w),south(s),east(e)) solo necesitamos escribir la inicial
frame.pack(fill='both',expand=1)
# Si ponemos fill en el eje de las x (es decir horizontal) el frame crecerá horizontalmente según agrandemos la ventana; igualmente pero vertical con y.
# El argumento expand hace que el frame crezca respetando la proporcion respecto al root. el 1 aqui es un True. Este parametro tiene en cuenta el fill
# por esto si ponemos y o x se expandirá horizontal o verticalmente, sin embargo si ponemos both lo hará en ambas dimensiones
frame.config(cursor="pirate")
# Con config podemos cambiar varias cosas del programa, en este caso vamos a añadir un cursor pirata que solo funcionará en el ancho y alto asignados
frame.config(bg="lightblue")
# Cambiar el color
frame.config(bd=25)
# Con esto asignamos un ancho de borde, pero para ello deberemos cambiar le tipo de borde cosa que se hace en la siguiente linea
frame.config(relief="sun")
# Cambia el tipo de borde


root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=15)
root.config(relief="ridge")
# Cambiando el frame por root los cambios de configuracion se aplican a la ventana de la app entera y no unicamente al marco designado





# Label -> Etiqueta donde podemos mostrar algun texto estático

# Entry -> Entradas sencillas para escribir un texto corto

# text - > Campo de texto multilinea para textos largos

# Button -> Botón sobre el cual el usuario puede hacer click

# Radio Button -> Button radial para marcar una opcion

# Check button -> boton cuadrado que se puede marcar con un tick

# Menu -> estructura de botones centrados en lc omposicion de menus

# Boxes y dialogs -> Permiten mostrar mensajes al usuario 

root.mainloop()
