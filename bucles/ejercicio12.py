# Escribir un programa en el que se pregunte al usuario por una frase y una letra,
# y muestre por pantalla el número de veces que aparece la letra en la frase.


frase = str(input("Introduce tu frase: "))


letra = (input("Calcular el numero de veces que aparece la letra: "))

y = 0

for i in frase:
    if i == letra:
        y += 1
    else:
        pass
print("la letra", letra, "aparece", y, "veces")