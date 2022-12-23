# Escribir un programa que pida al usuario dos números enteros
# y muestre por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos 
# por el usuario, y <c> y <r> son el cociente y el resto de la división entera respectivamente.


d1 = float(input("Introduce un numero: "))

d2 = float(input("Introduce un numero: "))

cociente = d1/d2

resto = d1%d2

print(round(d1), "entre", round(d2), "da un cociente", round(cociente,2), "y un resto", round(resto,2))