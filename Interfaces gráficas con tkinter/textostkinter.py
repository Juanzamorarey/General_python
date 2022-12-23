from tkinter import*
# Vamos a ver los formatos .text
root= Tk()

texto = Text(root)
texto.pack()
# Con esto tendremos una ventana en la que podemos escribir texto. Pero tiene unas lines y caracteres predefinidas. Para cambiarlo usamos width y height pero con numero de caracteres
# Es importante resaltar que lo que pongamos aqui será el número de caracteres, no el número de pixeles. Es decir width = caracteres por linea. Height = numero de lineas
texto.config(width= 30, height= 12,font=("TimesNewRoman",24),selectbackground="blue")
# En estos textos podemos usar los atributos que ya utilizamos en los campos de texto. A saber:
# .config(font=)
# padx/pady = 5 para poner margenes por arriba y por debajo
# selectbackground = "" indica un color para el texto cuando es seleccionado




root.mainloop()