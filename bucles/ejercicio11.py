# Escribir un programa que pida al usuario una palabra y
# luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

palabra = str(input("Introduce una palabra: "))

y = palabra[::-1] #Con esto le damos la vuelta al string [::-1]

n = 0

lista = []

for i in y:
    # print(y[n])
    n +=1
    lista.append(i)

print(str(lista))    
