from tkinter import*
from tkinter import messagebox as MessageBox
# Las ventanas emergentes no están por defecto en tkinet por este motivo debemos importarlas. No es necesario renombrarlas pero lo hace el profe por el formato
root = Tk()

def test():
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
    resultado= MessageBox.askretrycancel("Reintentar","No se puede conectar")
# Esta dará una ventana emergente que tendrá dos opciones: reintentar la acción o cancelar la acción de maner automática. Devuleve un booleano como valor:
    if resultado:
        root.destroy()



Button(root, text="Clícame",command=test).pack()


# Todas estas ventanas emergentes son únicamente de un tipo que muestra información y lleva a cabo una respuesta en algunos casos. 

root.mainloop()