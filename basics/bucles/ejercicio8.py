# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1

numero = int(input("Introduce un numero: "))

for i in range(numero):
    print(i,"\n")
    if i > 1:
        print(i,i+2,"\n")