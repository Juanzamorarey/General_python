from tkinter import *
# from tkinter import ttk
import tkinter as tk
import pandas as pd
import random
from tkinter.filedialog import askopenfile
import re

# Variables para almacenar
respuestas_correctas = []
palabra_frances = "Flashcard examples"
palabras_espannol = []
lista_ya_vistos = []
numero_aciertos = 0
numero_errores = 0
numero_consultas = 0 
dataframe_estudio = ""
col_l2 = ""
col_l1 = ""

def open_popup():
   top= Toplevel(ventana)
   top.geometry("500x250")
   top.title("Ajustes columnas")
   col_l2_var = tk.StringVar()
   col_l1_var = tk.StringVar()
   titulo = Label(top, text= "Introduce el nombre de tus columnas")
   titulo.place(x=15,y=10)
   len_extr = Label(top, text= "Lengua extranjera:")
   len_extr.place(x=25,y=40)
   col_l2_ent = tk.Entry(top, textvariable=col_l2_var)
   col_l2_ent.place(x=150,y=40)
   len_nat = Label(top, text= "Lengua nativa:")
   len_nat.place(x=25,y=70)
   col_l1_ent = tk.Entry(top, textvariable=col_l1_var)
   col_l1_ent.place(x=150,y=70)
   global col_l2 
   global col_l1 
   col_l2 = col_l2_ent.cget("text")
   col_l1 = col_l1_ent.cget("text")
   boton_accept = Button(top, text ='Accept', command = lambda:open_file(top))
   boton_accept.place(x=75,y=200)
   boton_generar.config(state="disabled")
   boton_comprobar.config(state="disabled")
#    boton_newCsv.place(x=25, y=300)


def open_file(top): 
    file = askopenfile(mode ='r', filetypes =[('CSV Files','*.csv')]) 
    if file is not None:
        global dataframe_estudio
        dataframe_estudio = file.name
        regex = r"\w*.csv"
        archivo_csv = re.findall(regex, dataframe_estudio)
        boton_generar.config(text="Generar nueva palabra",command=cambiar_texto, state="active")
        boton_comprobar.config(text="Comprobar",command=llamada_comprobador, state="active")
        boton_newCsv.config(text=f"Practicando traduccion {archivo_csv[0]}", state="disabled")
        top.destroy()
         
# Aqui se asimila el csv obteniendo el número máximo para generar números aleatorios

def numero_aleatorio():
    numero_aleatorio = random.randint(1,595)
    return numero_aleatorio

def palabra_random(numero_aleatorio):
    # numero_aleatorio = random.randint(1,num_max)  
    # lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/palabras_generales.csv")
    lista_palabras = pd.read_csv(dataframe_estudio)
    resultado = lista_palabras.iloc[[numero_aleatorio]]
    diccionario_df = resultado.to_dict()
    palabra_frances = diccionario_df["frances"][numero_aleatorio]
    resultado = palabra_frances
    palabras_espannol = diccionario_df["español"][numero_aleatorio]
    lista_posible_aciertos = palabras_espannol
    # print(lista_posible_aciertos)
    return resultado, lista_posible_aciertos
    

def comprobar_palabra(respuestas_correctas,numero_aciertos,numero_errores,numero_consultas):
    comprobador = []
    #Estadística
    numero_aciertos = total_correctas_ent.cget("text")
    numero_errores = total_incorrectas_ent.cget("text")
    numero_consultas = total_consultas_ent.cget("text")
    if isinstance(numero_aciertos, int) or isinstance(numero_errores, int) or isinstance(numero_consultas, int):
        pass
    else:
        numero_aciertos = 0
        numero_errores = 0
        numero_consultas = 0
    #Comrpobador
    introduccion_usuario = str(Intro_traduccion.get())
    respuesta_correcta = str(respuestas_correctas.get())
    if "," in respuesta_correcta:
        comprobador = respuesta_correcta.split()
    else:
        comprobador.append(str(respuesta_correcta))
    
    if introduccion_usuario in comprobador:
            lista_ya_vistos.append(0)
            numero_aciertos = int(numero_aciertos) + 1
            numero_consultas = int(numero_consultas) + 1
            cambiar_texto()
            correcto = "Correcto!!!"
            actualizar_estado(correcto)
    if introduccion_usuario not in comprobador:
            numero_errores = int(numero_errores) + 1
            numero_consultas = int(numero_consultas) + 1
            cambiar_texto()
            incorrecto = f"No es correcto. \n la respuesta correcta es: {respuesta_correcta}"
            actualizar_estado(incorrecto)
    actualizador_estadisticas(numero_aciertos,numero_errores,numero_consultas)    
    

def actualizar_estado(correccion):
    if "No" in correccion:
        estado_ent.config(text=correccion, background="red")
    else:
        estado_ent.config(text=correccion, background="green")


def cambiar_texto():
    numero_aleat = numero_aleatorio()
    info_flashcard = palabra_random(numero_aleat)
    palabra_frances.set(info_flashcard[0])
    respuestas_correctas.set(info_flashcard[1])
    # print(respuestas_correctas)

def llamada_comprobador():
    comprobar_palabra(respuestas_correctas,numero_aciertos,numero_errores,numero_consultas)
    # print(respuestas_correctas)

def actualizador_estadisticas(numero_aciertos,numero_errores,numero_consultas):
    total_correctas_ent.config(text=numero_aciertos)
    total_incorrectas_ent.config(text=numero_errores)
    total_consultas_ent.config(text=numero_consultas)

#Ventana
ventana = tk.Tk()
ventana.configure()
# Variables
palabra_frances = tk.StringVar()
palabra_frances.trace_add("write", cambiar_texto)
respuestas_correctas = tk.StringVar()
respuestas_correctas.trace_add("write", cambiar_texto)
resultado_comp = tk.StringVar()
resultado_comp.trace_add("write", llamada_comprobador)
estado_ent = tk.StringVar()
intro_usuario = tk.StringVar()


# Estadisticas
total_correctas_ent = tk.StringVar()
total_incorrectas_ent = tk.StringVar()
total_consultas_ent = tk.StringVar()
# consultas_correctas.trace_add("write", llamada_comprobador)
# consultas_incorrectas.trace_add("write", llamada_comprobador)
# consultas_totales.trace_add("write", llamada_comprobador)


ventana.title("Script de flashcards")
ventana.config(width=600, height=400)

#Lado de traducción
etiqueta_palabra_traducir = tk.Label(text="Palabra a traducir")
etiqueta_palabra_traducir.place(x=200, y=10)

etiqueta_busca_palabra = tk.Entry(textvariable=palabra_frances, state="disabled", font=("Calibri",14,"bold"))
etiqueta_busca_palabra.place(x=200, y=35)

etiqueta_palabra_traducir = tk.Label(text="Introduce la traducción:")
etiqueta_palabra_traducir.place(x=410, y=10)

Intro_traduccion = tk.Entry(textvariable=intro_usuario, font=("Calibri",14,"bold"))
Intro_traduccion.place(x=410, y=35, width=150)

boton_generar = tk.Button(text="Generar nueva palabra",command=cambiar_texto)
boton_generar.place(x=410, y=60)

boton_comprobar = tk.Button(text="Comprobar",command=llamada_comprobador)
boton_comprobar.place(x=410, y=90)


#Lado de estadísticas
total_consultas = tk.Label(text="Total de consultas:")
total_consultas.place(x=20, y=10)

total_consultas_ent = tk.Label(highlightthickness=2, text=total_consultas_ent, state="disabled", width=5)
total_consultas_ent.place(x=125, y=10)

total_correctas = tk.Label(text="Total acertadas:")
total_correctas.place(x=20, y=40)

total_correctas_ent = tk.Label(highlightthickness=2, text=total_correctas_ent, state="disabled", width=5)
total_correctas_ent.place(x=125, y=40)

total_incorrectas = tk.Label(text="Total errores:")
total_incorrectas.place(x=20, y=65)

total_incorrectas_ent = tk.Label(highlightthickness=2, text=total_incorrectas_ent, state="disabled", width=5)
total_incorrectas_ent.place(x=125, y=65)

# feedback

estado = tk.Label(text="Estado:")
estado.place(x=20, y=90)

estado_ent = tk.Label(highlightthickness=2,text=estado_ent, state="disabled", width=35,height=5, font=("Calibri",16, "bold"))
estado_ent.place(x=20, y=90)

boton_newCsv = Button(ventana, text ='Open CSV', command = lambda:open_popup())
boton_newCsv.place(x=25, y=300)

boton_salir = Button(ventana, text="Quit", command=ventana.destroy)
boton_salir.place(x=500, y=300)

ventana.mainloop() #Este debe ser siempre la línea de código final