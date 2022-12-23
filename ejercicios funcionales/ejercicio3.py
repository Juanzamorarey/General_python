# escribir una función que reciba otra función booleana y una lista, 
# y devuelva otra lista con los elementos de la lista que devuelvan True al aplicarles la función booleana.


def regueton(numero):
    if numero % 2 == 0:
            True
            return numero
    else:
        False
        return None


def funcion_booleana (function,lista):
    lista_nueva = []
    for i in lista:
        resultado = regueton(i)
        if resultado == None:
            pass
        else:
            lista_nueva.append(resultado)
    print(lista_nueva)

listassa = [1,2,3,4,5,6,7,8,9,10.5,10,21,34,56,76,34,21,54]

funcion_booleana(regueton,listassa)