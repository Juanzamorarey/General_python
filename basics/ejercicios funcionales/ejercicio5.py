# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud


def convertir_en_diccionario ():
    frase = input(str("Introduce tu frase: "))
    frase_dividida = frase.split()
    Longitudes = []
    for i in frase_dividida:
        longitud = len(i)
        Longitudes.append(longitud)
    for diccionario in zip(frase_dividida,Longitudes):
        print(diccionario)
    

convertir_en_diccionario()