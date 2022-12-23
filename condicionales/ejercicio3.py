# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.

dividendo = int(input("Introduce el dividendo: "))

divisor = int(input("Introduce el divisor: "))

if divisor == 0:
    print("Error. No es posible realizar la division")
else: 
    print(dividendo/divisor)