# Escribir una función que reciba una muestra de números en una lista y devuelva su media.
lista = [1,2,3,4,5,6,7,8,9,10]
lista2 = [14,23,59,87,34]

def media(lista):
    resultado = sum(lista)/len(lista)
    return resultado


print(media(lista))
print(media(lista2))