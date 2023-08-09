# Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
# Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>


#diccionario[clave] = valor AÑADE 
#del diccionario[clave] = valor ELIMINA ELEMENTO



persona = {'nombre':'','edad':'','direccion':'','telefono':''}


nombre = str(input("¿Cómo te llamas?"))
persona[nombre] = nombre
edad = int(input("¿Cuántos años tienes?"))
persona[edad] = edad
direccion = str(input("¿Dónde vives?"))
persona[direccion] = direccion
telefono = str(input("¿Cuál es tu número de teléfono?"))
persona[telefono] = telefono

print(persona[nombre], "tiene", persona[edad], "años, vive en", persona[direccion], "y su número de teléfono es" , persona[telefono])