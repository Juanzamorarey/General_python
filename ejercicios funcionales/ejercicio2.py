# Escribir una función que reciba otra función y una lista, 
# y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.
contador = 0
def por2 (lista_sin_multiplicar):
    nueva_lista = []
    for i in lista_sin_multiplicar:
        multiplicacion = i*2
        nueva_lista.append(multiplicacion)     

    return nueva_lista



def funcion (function, lista):
        print(function(lista))

listassa = [1,2,3]
funcion(por2,listassa)


# Cosas a tener en cuenta: Si usamos una variable i en el bucle for, dicha variable adquiere el valor de los elementos dentro de la lista:
# NUNCA ADQUIERE EL VALOR DE LA POSICIÓN
lista = [1,2,3]
print(lista)
for i in [1,2,3]:
    print("ahora i vale",i," y su multiplicación es",i*2)