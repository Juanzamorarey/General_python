#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces

palabra = str(input("introduce una palabra: "))

i = int(0)

while i <= 10:
    print(palabra)
    i += 1
    if i == 10:
        break