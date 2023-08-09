# Escribir un programa que pida al usuario un número entero positivo y
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

numero = int(input("Introduce tu número:"))

i = 0
y = 0
lista = [numero]

while i < numero:  
    y +=1
    lista.append(numero - y)
    i += 1
else:
    print(lista)
