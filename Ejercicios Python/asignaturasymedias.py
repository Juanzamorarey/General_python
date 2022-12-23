from tkinter import*


def nueva_asignatura():
# Creador de asignatura
    h = int(n1.get())
    p = 2
    while p < h:
        i = Frame(root)
        X = int(2)
        i.grid(row=X,column=0,sticky="new")
        i.rowconfigure(0,weight=1)
        i.columnconfigure(0,weight=1)
        X + 1
        p + 1
    # Tienes la variable n1 que corresponde al numero de asignaturas, hay que hacer que la función genere tantos marcos como número de asignaturas
    
    
    asignatura_label = Label(i,text="Asignatura:")
    asignatura_label.pack(side="left")
    asignatura_label.config(font=("calibri",16))

    asignatura_texto = Entry(i)
    asignatura_texto.config(justify="left",state="normal",bg="orange",bd=15,relief="groove")
    asignatura_texto.rowconfigure(0,weight=1)
    asignatura_texto.columnconfigure(0,weight=1)
    asignatura_texto.pack(side="right")

# # Creador de rama
#     rama_label = Label(marco_rama,text="rama:")

#     rama = Frame(root)
#     rama.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
#     rama.grid(row=0,column=1,sticky="new")
#     rama.rowconfigure(0,weight=1)
#     rama.columnconfigure(1,weight=1)

# # Creador de nota
#     rama_nota = Label(marco_nota,text="nota:")

#     nota = Frame(root)
#     nota.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
#     nota.grid(row=0,column=2,sticky="new")
#     nota.rowconfigure(0,weight=1)
#     nota.columnconfigure(2,weight=1)

def media_total():
    pass
def media_ciencias():
    pass
def media_letras():
    pass


# Raíz
root = Tk()
root.title("Asignaturas y medias")
root.resizable(1,1)
root.config(bg="black",bd=20,relief="sunken")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.rowconfigure(0,weight=1)
root.columnconfigure(2,weight=1)

n1=StringVar()
n2=StringVar()



# Numero de asignaturas:
numeroasignaturas = Label(root,text="Introduce numero de asignaturas:").grid(row=0,column=0,sticky="new")
numero_asignaturas = Entry(root,textvariable=n1).grid(row=0,column=1,sticky="new")


# Marco de asignatura
marco_asignatura = Frame(root)
marco_asignatura.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_asignatura.grid(row=1,column=0,sticky="new")
marco_asignatura.rowconfigure(0,weight=1)
marco_asignatura.columnconfigure(0,weight=1)

# Marco de rama
marco_rama = Frame(root)
marco_rama.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_rama.grid(row=1,column=1,sticky="new")
marco_rama.rowconfigure(0,weight=1)
marco_rama.columnconfigure(1,weight=1)

# Marco de nota
marco_nota = Frame(root)
marco_nota.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_nota.grid(row=1,column=2,sticky="new")
marco_nota.rowconfigure(0,weight=1)
marco_nota.columnconfigure(2,weight=1)

# Label asignaturas

asignaturas = Label(marco_asignatura,text="Asignaturas")
asignaturas.config(font=('calibri','20'),fg='black')
asignaturas.pack(anchor="n")

# Label ramas

rama = Label(marco_rama,text="   Rama    ")
rama.config(font=('calibri','20'),fg='black')
rama.pack(anchor='n')

# Label notas

nota = Label(marco_nota,text="   Nota    ")
nota.config(font=('calibri','20'),fg='black')
nota.pack(anchor='n')

# Boton para crear nueva asignatura
# while fila < numero_asignaturas:
Button(root, text="Generar asignaturas", command=nueva_asignatura).grid(row=1,column=3,sticky="new")#Corregir la posicion del boton usando el metodo grid. Grande y abajo del todo
Button(root, text="Nota media:", command=media_total).grid(row=2,column=3,sticky="new")#Corregir la posicion del boton usando el metodo grid. Grande y abajo del todo
Button(root, text="Nota media ciencias:", command=media_ciencias).grid(row=3,column=3,sticky="new")#Corregir la posicion del boton usando el metodo grid. Grande y abajo del todo
Button(root, text="Nota media letras:", command=media_letras).grid(row=4,column=3,sticky="new")#Corregir la posicion del boton usando el metodo grid. Grande y abajo del todo

root.mainloop()
