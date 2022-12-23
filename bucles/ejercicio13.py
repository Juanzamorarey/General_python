# Escribir un programa que muestre el eco de todo
# lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

i = str()

while i != "salir":
    i = input("habla y habrá eco: ")
    print(i)
else:
    print("has salido del bucle")

