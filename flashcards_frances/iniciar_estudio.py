# Vamos a mostrar una palabra en francés y habrá que escribirla en español
import pandas as pd
import random
import tkinter as tk
from tkinter import ttk

def comparar_palabras(lista_palabras, num_max):
    introduce_usuario = ""
    lista_ya_vistos = []
    numero_aciertos = 0
    numero_errores = 0
    numero_consultas = 0
    while introduce_usuario != "exit":
        numero_aleatorio = random.randint(1,num_max)
        if numero_aleatorio in lista_ya_vistos:
            print("palabra vista")
        else:
            resultado = lista_palabras.iloc[[numero_aleatorio]]
            diccionario_df = resultado.to_dict()
            palabra_frances = diccionario_df["frances"][numero_aleatorio]
            palabras_espannol = diccionario_df["español"][numero_aleatorio]
            lista_posible_aciertos = palabras_espannol.split()
            print(f"La palabra en francés es : {palabra_frances}\n")
            introduce_usuario = input("Introduce su traducción en español: ")                
            if introduce_usuario in lista_posible_aciertos:
                print("Correcto\n")
                lista_ya_vistos.append(0)
                numero_aciertos+=1
                numero_consultas+=1
            if introduce_usuario == "exit":
                porcentaje_acierto = numero_aciertos/numero_consultas * 100
                fin = f"""Tus resultados son:\n
                    palabras acertadas: {numero_aciertos}\n
                    palabras erróneas: {numero_errores}\n
                    total de consutlas: {numero_consultas}
                    Porcentaje de acierto: {porcentaje_acierto}%"""
                return fin
            if introduce_usuario not in lista_posible_aciertos:
                print("No es correcto\n")
                print(f"La palabras aceptadas para esta traducción son: {lista_posible_aciertos}")
                numero_errores+=1
                numero_consultas+=1
        

# comparar_palabras()

def ejecutar_programa():
    print("Vamos a practicar las palabras del francés, en cualquier momento introduce -exit- para salir del programa y ver tus resultados")
    seleccion = input("Elige qué quieres practicar:\n 1. Verbos \n 2. Nombres \n 3.Adjetivos \n 4.Todas las palabras juntas ")
    if seleccion == "1":
        lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/verbos.csv")
        num_max = 231
    if seleccion == "2":
        lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/nombres.csv")
        num_max = 292
    if seleccion == "3":
        lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/adjetivos.csv")
        num_max = 74
    if seleccion == "4":
        lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/palabras_generales.csv")
        num_max = 595  
    # lista_palabras = pd.read_csv("C:/Users/juan_/Desktop/scripts del dia a dia/flashcards_frances/probador.csv")
    programa = comparar_palabras(lista_palabras, num_max)
    print(programa)

if __name__ == '__main__':
    ejecutar_programa()