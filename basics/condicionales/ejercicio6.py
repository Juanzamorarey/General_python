# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, 
# y muestre por pantalla el grupo que le corresponde.


nombre = str(input("¿Cómo te llamas?"))

sexo = str(input("¿Eres hombre o mujer?"))

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l"," m", "n", "ñ", "o","p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

if sexo == str("mujer"):
    if nombre[0].lower() <= "m":
        print("Estás en el grupo A")
    else:
        print("Estás en el grupo B")

if sexo == str("hombre"):
    if nombre[0].lower() > "m":
        print("estás en el grupo A")
    else:
        print("Estás en el grupo B")



