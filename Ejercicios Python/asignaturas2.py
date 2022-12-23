from tkinter import*

lista = []
notas = 0
def numero_asignaturas():
# Creador de asignatura
    c = 1    
    h = 10
    v = 90
    # Variables para radiobuttons
    p = 0
    j = 0
    operador = float(nasignaturas.get())
    while c <= operador:
        c += 1
        v += 30
        p += 1
        j += 100
        asignaturas = Frame(root)
        asignaturas.config(width=2000,height=2000,bg="white",bd=5,relief="ridge")
        nombre_asignaturas = Entry(asignaturas,justify="center",font=("calibri",12),state="normal")
        nombre_asignaturas.pack(anchor='n')
        asignaturas.place(x=h,y=v)

        # Marco de la rama:
        marco_rama = Frame(root)
        marco_rama.config(width=580,height=40,bg="white",bd=5,relief="ridge")
        marco_rama.place(x= h + 390, y= v)
        contenedor = StringVar() #Al poner aquí esta variable se asigna a cada uno de los nuevos frames, haciendo que los radiobuttones sean excluyentes
        Radiobutton(marco_rama, text="Ciencias",value=p,variable=contenedor,command=rama).pack(side="left",anchor="n")
        Radiobutton(marco_rama, text="Letras",value=j,variable=contenedor,command=rama).pack(side="right",anchor="n")

        # Marco de la nota:
        marco_nota = Frame(root)
        marco_nota.config(width=300,height=40,bg="white",bd=5,relief="ridge")
        marco_nota.place(x= h + 780, y= v)

        nota_2 = Label(marco_nota, text="Nota:")
        nota_2.config(font=('calibri','12'),fg='black')
        nota_2.pack(side="left",anchor='w')
        nota = IntVar()
        nota_asignatura = Entry(marco_nota,justify="center",font=("calibri",12),state="normal",textvariable=nota).pack(side="right",anchor='n')
    
    def calcular_media():
        if nota == 0:
            pass
        else:
            resultado = nota.get()
            lista_media = []
            lista_media.append(resultado)
            media = sum(lista_media)/c
            nmedia = Entry(root,justify="left",textvariable=media,state="disabled")

    # Boton para calcular media
    Button(root, text="Calcular media total",command = calcular_media).place(x=1100,y=130)
    nmedia = Entry(root,justify="left",state="disabled")
    nmedia.place(x=1250,y=130)
    nmedia.config(justify="center",state="normal")

    # Boton para calcular media ciencias
    Button(root, text="Calcular media ciencias").place(x=1100,y=160)
    nmedia_ciencias = Entry(root,justify="left",textvariable=nciencias,state="disabled")
    nmedia_ciencias.place(x=1250,y=160)
    nmedia_ciencias.config(justify="center",state="normal")

    # Boton para calcular media letras
    Button(root, text="Calcular media letras").place(x=1100,y=190)
    nmedia_letras = Entry(root,justify="left",textvariable=nletras,state="disabled")
    nmedia_letras.place(x=1250,y=190)
    nmedia_letras.config(justify="center",state="normal")

        
    
def media_ciencias():
    pass
def media_letras():
    pass


# Raíz
root = Tk()
root.title("Asignaturas y medias")
root.resizable(1,1)
root.config(bg="black",bd=20,relief="sunken",width=1500, height=500)


n1 = StringVar()
nmedia = StringVar()
nciencias = StringVar()
nletras = StringVar()
resultado_global = StringVar()
nota = IntVar()

# Marco de asignatura
marco_asignatura = Frame(root)
marco_asignatura.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_asignatura.place(x=10,y=10)


# Marco de rama
marco_rama = Frame(root)
marco_rama.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_rama.place(x=400,y=10)

# Marco de nota
marco_nota = Frame(root)
marco_nota.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
marco_nota.place(x=790,y=10)

# Marco n de asignaturas
n_asignaturas = Frame(root)
n_asignaturas.config(width=2000,height=2000,bg="white",bd=15,relief="ridge")
n_asignaturas.place(x=1100,y=10)


# Label asignaturas
asignaturas = Label(marco_asignatura,text="Nombre")
asignaturas.config(font=('calibri','20'),fg='black')
asignaturas.pack(anchor="n")

# Label ramas
rama = Label(marco_rama,text="Rama")
rama.config(font=('calibri','20'),fg='black')
rama.pack(anchor='n')

# Label notas
nota = Label(marco_nota,text="Nota")
nota.config(font=('calibri','20'),fg='black')
nota.pack(anchor='n')

# Label n_asignaturas
nota = Label(n_asignaturas,text="Numero de asignaturas")
nota.config(font=('calibri','20'),fg='black')
nota.pack(anchor='n')



# Boton para generar nuevas asignaturas
Button(root, text="Generar asignaturas", command=numero_asignaturas).place(x=1100,y=100)
nasignaturas = Entry(root,justify="left",textvariable=n1)
nasignaturas.place(x=1250,y=100)
nasignaturas.config(justify="center",state="normal")


# # Boton para calcular media
# Button(root, text="Calcular media total",command=numero_asignaturas).place(x=1100,y=130)
# nmedia = Entry(root,justify="left",textvariable=resultado_global.get(),state="disabled")
# nmedia.place(x=1250,y=130)
# nmedia.config(justify="center",state="normal")

# # Boton para calcular media ciencias
# Button(root, text="Calcular media ciencias").place(x=1100,y=160)
# nmedia_ciencias = Entry(root,justify="left",textvariable=nciencias,state="disabled")
# nmedia_ciencias.place(x=1250,y=160)
# nmedia_ciencias.config(justify="center",state="normal")

# # Boton para calcular media letras
# Button(root, text="Calcular media letras").place(x=1100,y=190)
# nmedia_letras = Entry(root,justify="left",textvariable=nletras,state="disabled")
# nmedia_letras.place(x=1250,y=190)
# nmedia_letras.config(justify="center",state="normal")



root.mainloop()