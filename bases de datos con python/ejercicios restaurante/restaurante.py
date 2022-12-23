import sqlite3
from tkinter import *
    

# def crear_bd():
#     conexion = sqlite3.connect("restaurante.db")
#     cursor = conexion.cursor()
#     try:
#         cursor.execute('''CREATE TABLE categoria(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nombre VARCHAR(100) UNIQUE NOT NULL)''')
#     except:
#         print("las tablas ya existen")
#     else:
#         print("todo ha ido bien")


#     try:
#         cursor.execute('''CREATE TABLE plato(
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nombre VARCHAR(100) UNIQUE NOT NULL,
#                 categoria_id INTEGER NOT NULL,
#                 FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
#     except:
#         print("las tablas ya existen")
#     else:
#         print("todo ha ido bien")

#     conexion.close()

# crear_bd()

# def agregar_categoria():
#     conexion = sqlite3.connect("restaurante.db")
#     cursor = conexion.cursor()
#     nombre_categoria = input("Introduce un nombre de categoría: ")
#     try:
#         cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(nombre_categoria))
#     except:
#         print("esa categoría ya existe")
#     else:
#         print("se ha añadido la categoría")
    
#     conexion.commit()
#     conexion.close()

# agregar_categoria()
# agregar_categoria()
# agregar_categoria()
# agregar_categoria()


# def agregar_plato():
#     conexion = sqlite3.connect("restaurante.db")
#     cursor = conexion.cursor()

#     cursor.execute("SELECT * FROM categoria")
#     categorias_seleccionables = cursor.fetchall()
#     for categoria_seleccionada in categorias_seleccionables:
#         print(categoria_seleccionada)
#     try:
#         numero_seleccionador = input("Introduce el numero de categoria a seleccionar")
#         categoria_seleccionada = cursor.execute("SELECT * FROM categoria WHERE id = '{}'".format(numero_seleccionador))
#         nombre_plato = input("Introduce el nuevo plato: ")
#         cursor.execute("INSERT INTO plato VALUES (null,'{}', {})".format(nombre_plato,numero_seleccionador))
#     except:
#         print("El plato {} ya existe".format(nombre_plato))
#     else:
#         print("plato añadido correctamente")

#     conexion.commit()
#     conexion.close()


# agregar_plato()
# agregar_plato()
# agregar_plato()
# agregar_plato()


# def mostrar_menu():
#     conexion = sqlite3.connect("restaurante.db")
#     cursor = conexion.cursor()

#     categorias = cursor.execute("SELECT * FROM categoria").fetchall()
#     for categoria in categorias:
#         print(categoria[1])
#         platos = cursor.execute(
#             "SELECT * FROM plato WHERE categoria_id={}".format(
#                 categoria[0])).fetchall()
#         for plato in platos:
#             print ("\t{}".format(plato[1]))

#     conexion.commit()
#     conexion.close()

# # mostrar_menu()

root = Tk()
root.title("Il Siciliano")
root.resizable(0,0)
root.config(bd=25, relief="sunken")


Label(root, text= "Ristorante: Il siciliano", fg="darkgreen", font=(
    "Times New Roman",28,"bold italic")).pack()
Label(root, text= "Menú de hoy", fg="darkgreen", font=(
    "Times New Roman",24,"bold italic")).pack()

Label(root,text="").pack()

conexion = sqlite3.connect("restaurante.db")
cursor = conexion.cursor()

categorias = cursor.execute("SELECT * FROM categoria").fetchall()
for categoria in categorias:
    Label(root, text=categoria[1],fg="black",font=(
        "Times New Roman",20,"bold italic")).pack()
    platos = cursor.execute(
        "Select * FROM plato WHERE categoria_id={}".format(
            categoria[0])).fetchall()
    for plato in platos:
        Label(root,text=plato[1],fg="gray",font=("Verdana",25,"italic")).pack()
    Label(root,text="").pack()

conexion.close

Label(root, text="20 $", fg="darkgreen",font=("Times New Roman",20,"bold italic")).pack(side="right")

root.mainloop()