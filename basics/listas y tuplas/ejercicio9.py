# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.


palabra = str(input("Introduce tu palabra: "))

a = 0
e = 0
i = 0
o = 0
u = 0


for y in palabra:
    if y == "a":
        a += 1
    elif y == "e":
        e += 1
    elif y == "i":
        i += 1
    elif y == "o":
        o += 1
    elif y == "u":
        u += 1

print("Tu palabra tiene:\n{} veces la vocal a \n{} veces la vocal e \n{} veces la vocal i \n{} veces la vocal o \n{} veces la vocal u".format(a,e,i,o,u))