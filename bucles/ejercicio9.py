# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

entrada = str(input("Crea tu contraseña: "))

contraseña = input("Introduce tu contraseña para acceder: ") 

while contraseña != entrada:
    print("Contraseña denegada")
    contraseña = str(input("Introduce tu contraseña: "))
else:
    print("Contraseña correcta. Acceso concedido")