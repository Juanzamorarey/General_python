# Escribir un programa que pida al usuario un número entero y 
# muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
# *
# **
# ***
# ****
# *****

numero = int(input("Introduce la altura de tu triangulo: "))


for i in range(numero+1): #i es lo que ocurre el numero de veces del range
    y = "*"
    print(y*i)
    