# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la 
# contraseña introducida por el usuario coincide con la guardada en la variable
# sin tener en cuenta mayúsculas y minúsculas.

contraseña = str(input("Introduce tu contraseña: "))

acceso = str(input("introduce tu contraseña: "))

if contraseña.lower() == acceso.lower():
    print("Acceso concedido")
else: 
    print("Tu contraseña es: ", contraseña, "y has escrito:", acceso,"por lo que tu acceso ha sido denegado")
