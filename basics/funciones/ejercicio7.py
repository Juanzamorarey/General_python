# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

lista = [1,2,3,4,5,6,7,8,9,10]

def hacer_cuadrados(lista):
    lista_cuadrados = []
    for i in lista:
        resultado = i**2
        lista_cuadrados.append(resultado)
    return lista_cuadrados

print(hacer_cuadrados(lista))