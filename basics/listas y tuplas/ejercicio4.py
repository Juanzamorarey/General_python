# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.

# Suponemos que el numero ganador tiene 5 cifras: ej 14325


lista = []
x= 0

for i in range(5):
    numero = int(input("Introduce la {} cifra del numero ganador : ".format(i+ 1)))
    i += 1
    lista.append(numero)

for x in range(10):
    if x in lista:
        print(x)
    else:
        pass
        x +=1



