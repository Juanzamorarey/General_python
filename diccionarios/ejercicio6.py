# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

agenda = {}

pregunta = input("Quieres añadir un nuevo contacto?")
if pregunta == "si":
    intro_nombre = input("¿Cómo se llama la persona?")
    agenda.setdefault('nombre',intro_nombre)
    intro_telefono = int(input("Cuál es su numero de teléfono?"))
    agenda.setdefault('numero',intro_telefono)
    intro_correo = input("¿Cuál es su correo electrónico?")
    agenda.setdefault('correo',intro_correo)
    print(agenda)
elif pregunta == "no":
    print("Tó chill")
else: 
    print("No entiendo que dices")

    