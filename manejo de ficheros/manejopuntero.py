from io import open
texto = "Una linea con texto \nOtra línea con texto" #Imaginemos que queremos guardar esto en un fichero

#     fichero = open('fichero.txt','r')
#     fichero.seek(10)#Esto indica que el putnero se sitúe en el caracter número 10
# #Si ahora hacemos un fichero.read() veremos que se devuelve todo el contenido a partir de donde se encuentra el puntero.
#     fichero.read()
# #Si volvemos a darle a .read() ya no habrá nada porque se ha situado el puntero al final del texto
#     fichero.seek(0)#vuelve al principio
#     fichero.read(5)#Con esto leemos desde la posición 0 hasta el 5

# # (por ejemplo podríamos averiguar la longitud del texto y situar el puntero en medio para leer a partir de ahí)

#     texto = fichero.read()
#     fichero.seek( len(texto)/2 )#Estamos en el medio
#     fichero.read()#Ahora se lee desde la mitad porque el fichero estña en el medio

# # Si quisiera situarme por líneas tendría que usar readline(). Por ejemplo para leer hasta el final de la primera linea:
#     fichero.seek( len(fichero.readline()))#Al no pasar argumentos a readlines toma la primera línea y sitúa el fichero al final
# #Es importante ser conscientes en todo momento de donde se encunetra nuestro cursor


# Si quisieramos crera un fichero y colocarlo en modo append y trabajar desde la primera posicion
    # fichero = open('fichero.txt','r+')#El modo r+ significa lectura y escritura
    # fichero.write("regueton")
    # fichero.close()
# El r+ entonces resulta equivalente a hacer un append y situar el puntero al principio. 

# Imaginemos ahora que queremos modificar una de las líneas concretas.
# Deberíamos abrir el fichero, separar las líneas de texto, acceder a la lista de líneas, modificar aquella que queremos y volver a escribir el contenido´

fichero = open("fichero.txt",'r+')
lineas = fichero.readlines()
lineas[2] = "Esta línea la he modificado en memoria\n"
#Ahora que hemos modificado la linea volvemos a escribir todo el contenido encima
# Para ello tenemos lo siguiente
fichero.seek(0)#Situamos el puntero
fichero.writelines(lineas)#Sobreescribimos el fichero con toda la información guardada en líneas
fichero.close()#cerramos el fichero

#De esta manera hemos modificado un fichero completo utilizando el modo r+ y los comanods readlines() y writelines()