# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.


lista_numeros = [30,45,67,23,56]
import math

def operaciones_estadísticas(lista):
    diccionario = {}
    media = sum(lista)/len(lista)
    diccionario["media"] = round(media,2)
    for i in lista:
        lista_varianza = []
        lista_varianza.append((i - media)**2)
    varianza = sum(lista_varianza)
    diccionario["varianza"] = round(varianza,2)
    desviacion_típica = math.sqrt(varianza)# esto es del modulo math y sirve para hacer raíces cuadradas
    diccionario["desviacion_típica"] = round(desviacion_típica,2)
    print(diccionario)

operaciones_estadísticas(lista_numeros)
