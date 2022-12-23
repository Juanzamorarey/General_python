regueton = 10
papasito = "Soy un papasito bien sexy"

print("'{papasito}' es una cadena, mientras que '{regueton}' es un numero entero".format(regueton=regueton,papasito=papasito))

# Una manera de usar el format que puede ser útil es poniendolo dentro del print con llaves y entre comillas simples
# dentro de las llaves podemos escribir una clave y, dentro del format, asignar a la clave la variable que queremos en ese espacio

# Con format podemos modificar el formato en el que se muestran las variables. Por ejemplo cambiando su posición

variable = "Este texto es lo que queremos que se muestre"

print("{:^30}".format(variable)) #Alinea al centro dejando 15 espacios a cada lado

print("{:>30}".format(variable)) #Alinea a la derecha dejando 30 espacios a la izquierda

print("{:<30}".format(variable)) #Alinea a la izquierda dejando 30 espacios a la derecha (viene asi por defecto)

print("{:.3}".format(variable)) #Parte la cadena, solo se mostrarán los tres primeros caracteres. Es un truncamiento de caracteres

print("{:<30.3}".format(variable)) #Con esto juntamos los dos procedimientos. El alineamiento y el trunacmiento

# Vamos a ver algunos ejemplos de formateos de numeros enteros

print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))
# Como se ve en el output los 3 numeros se han alineado a cuatro digitos, de modo que podemos ejecutar la suma a la derecha
# Su pusieramos antes del 4d un caracter se alinearian pero con ese caracter en medio
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))
# Ahora en vez de espacios aparecen 0

# Para recortar decimales también podemos usar format
print("{:.2f}".format(3.1415926)) #El 2f junto con el truncamiento hace que se muestren solo dos decimales
print("{:.2f}".format(153.21))
# Si quisiéramos alinear estos números agrupando enteros y decimales por separado
# tendríamos que escribir el número total de caracteres a alinear y cuántos flotantes hay en suma
print("{:7.2f}".format(3.1415926))
print("{:7.2f}".format(153.21)) #El 7 indica que habrá un total de 7 caracteres de los cuales 2 son flotantes