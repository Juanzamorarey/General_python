from tkinter import*
# Vamos a crear un menú. Estos menús son los mismos que aparecen arriva con file, Edit, etc. Despliegan una serie de opciones y nosotros seleccionamos la que queremos
root = Tk()

menubar = Menu(root)#El menu no se empaqueta porque siempre está en la misma posicion. Se añade en la configuracion de la root
root.config(menu=menubar) 
# Los menus tienen submenus es por eso importante que aclaremos que el principal se suele llamar menubar a efectos de no confundirlo con los otros submenus

# Vamos a crear un menu de fichero, otro de editar y un último de ayuda.

filemenu = Menu(menubar,tearoff=0)#Lo añadimos a menubar porque va a ser un submenu de menubar
filemenu.add_command(label="Nuevo")#De esta manera añadimos opciones a los submenus 
filemenu.add_command(label="Abrir") 
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()#De esta manera añadimos un separador dentro del submenu 
filemenu.add_command(label="Salir",command=root.quit)#De esta manera implementamos directamente la accion de salir .quit 


editmenu = Menu(menubar,tearoff=0)#Lo añadimos a menubar porque va a ser un submenu de menubar
editmenu.add_command(label="Cortar")#De esta manera añadimos opciones a los submenus 
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")


helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="Ayuda")#De esta manera añadimos opciones a los submenus 
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")#De esta manera añadimos opciones a los submenus 

# Para evitar la ejecución de una ventana extra que molesta se debe añadir a estos menus el tearoff=0, que eliminará esta ventana y nos dejará permanecer en la interfaz
#Ahora unicamente habría que añadir acciones a estos submenus de modo que realziaran alguna función cuando son seleccionados

menubar.add_cascade(label="Archivo", menu=filemenu)
# El metodo add_cascade añade menus en forma de cascada y toma de parametros primer el nombre (label="Arhcivo") y después el submenú en cuestión, en este caso filemenu
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)
# Para evitar la ejecución de una ventana extra que molesta se debe añadir a estos menus el tearoff=0, que eliminará esta ventana y nos dejará permanecer en la interfaz


root.mainloop()