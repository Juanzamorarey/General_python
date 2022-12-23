# Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input("introduce tu numero: "))


i = 0

while i < numero:
    i += 1
    if i % 2 != 0:
        print(i)