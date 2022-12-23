# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range(11): #Tiene que ser 11 porque la primera vez es la tabla del 0
    if i == 0:
        pass
    else:
        print(
            i*1,
            i*2,
            i*3,
            i*4,
            i*5,
            i*6,
            i*7,
            i*8,
            i*9,
            i*10,
        )
