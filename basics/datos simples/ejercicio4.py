#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

nombre = input("introduce un nombre: ")

numero = input("introduce un número entero: ")


i = 0
while i < int(numero):
    i +=1
    print(nombre, "\n")

    

