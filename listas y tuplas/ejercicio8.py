# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.


palabra = str(input("Introduce tu palabra: "))

if palabra == palabra[::-1]:
    print("Tu palabra es un palíndromo")
else:
    print("Tu palabra no es un palíndromo")