# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

numero = int(input("introduce un numero entero: "))

while numero % numero != 0 or numero % 2 == 0 :
    print("Tu numero no es primo marica")
    numero = int(input("introduce un numero entero: "))
else: 
    print("Tu numero es primo")