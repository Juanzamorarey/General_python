from tkinter import *

import nltk 
from nltk import sent_tokenize
from nltk import PunktSentenceTokenizer


texto_entrenamiento = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(texto_entrenamiento)
tokenizado = custom_sent_tokenizer.tokenize(frase)



def analizar():
    print(sent_tokenize(str(frase_analizada)))


root = Tk()

frase = StringVar()

frase_analizada = frase.get()

root.title("Analizador sintáctico")

label = Label(root, text="Frase:")
label.grid(row=0,column=0,sticky="e",padx=5,pady=5)


entry1 = Entry(root)
entry1.grid(row=0,column=1,padx=5,pady=5)
entry1.config(justify="center",state="normal",textvariable=frase)


frame = Frame(root,width=80,height=80).grid(row=1,column=0,sticky="e",padx=5,pady=5)

Button(frame, text="Analizar", command=analizar).grid(row=1,column=0,sticky="e",padx=5,pady=5)



root.mainloop()