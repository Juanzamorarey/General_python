# A través del manejo de ficheros podremos crear programas que persistan al tiempo de modo que podamos cerrar un programa y volver
# a abrirlo para trabajar con él. 
# Existen dos tipos de persistencia básicas: con ficheros o con bases de datos
# La extensión de un fichero indica que tipo de fichero es, de modo que podemos identificar varios ficheros de un mismo tipo.


# # Con un fichero podemos:
# ->Abrir: añade información al fichero
# ->crear
# ->Extender
# ->Cerrar

# Uno de los conceptos mas importantes es el puntero del fichero EL cual debe estar al final para no sobreescribir datos del fichero
# Por último debemos distinguir entre ficheros de texto (los que veremos) y ficheros binarios (donde la información se guarda en binario
# y cuya utilizacion es mas compleja, de todos modos se verá en el curso mediante el módulo pickle).

from io import open
# Esto es sumamente importante para que funcione correctamente el manejo de ficheros. Esto se debe hacer siempre desde
# el script para que funcionen todas las cosas que vamos a ver en este curso. 

texto = "Una linea con texto \nOtra línea con texto" #Imaginemos que queremos guardar esto en un fichero
# Para hacerlo debemos primero crear el fichero
    # fichero = open('fichero.txt','w')#IMPORTANTE: SI ABRIMOS UN FICHERO QUE YA EXISTE EN ESTE MODO SE BORRA LO QUE CONTIENE
#De esta manera creamos un fichero. La funcion open toma dos argumentos:
# El primero que toma es el tipo de fichero y el nombre, y el segundo el modo en el que se abrirá el fichero.
# En este caso se trata del modo de escritura.
    # fichero.write(texto)
# # Ahora que tenemos este fichero creado y abierto le añadimos, mediante el metodo write, 
# # El texto que tenemos en la variable que hemos creado.
    # fichero.close() 
# Es importante recordar que cada vez que abramos un fichero deberemos cerrarlo después

#Al cerrar y reabrir el fichero estamos realizando algo redundante pero se utiliza así para la explicación.


# Si quisieramos abrir un fichero sin reescribir toda la información que contiene tendríamos que abrirlo en modo lectura
    # fichero = open("fichero.txt",'r')#apertura en modo lectura

    # texto = fichero.read()
#Esto lee totalmente el contenido del fichero y lo guarda en una variable(IMPORTANTE)
    # fichero.close()
    # print(texto)

# Para almacenar todas las lineas del fichero en una 
# lista podemos crearla y modificar las lineas trabajando de manera mucho mas comoda
    # fichero = open("fichero.txt",'r')
    # líneas = fichero.readlines()#Con readlines() hacemos que en la varibale se almacenen las lineas que hayamos escrito en el fichero en formato lista
    # fichero.close()
    # print(líneas)#COmo vemos ahora se trata de una lista y tiene todas las propiedades de las mismas
    # print(líneas[0])#Ejemplo


# Imaginemos que ahora queremos añadir una nueva línea a este fichero. Para ello debemos usar el modo append
    # fichero = open("fichero.txt",'a')#modo append, el puntero se pone al final, no al principio como en el write, por lo que no sobreescribe información
    # fichero.write('\nCuarta línea del fichero')#Esto se añade al fichero justo al final
    # fichero.close()
#No se puede abrir un fichero en modo lectura si este no existe. EN cambio en los modos append o w se crea por defecto vacío.


# Se puede leer también el contenido por partes, no todo de golpe, ejemplo:
    # fichero = open("fichero.txt",'a')
    # fichero = open("fichero.txt",'r')
    # l = fichero.readline()#Este metodo lee la primera linea. Si lo hicieramos mas veces, aparecerían las líneas sucesivas
# Lo que estamos haciendo es desplazar el puntero al final de las diferentes líneas.
#l #Si lo ejecutáramos hasta el final daría de output una línea vacía.
# fichero.close()

#También se puede hacer esto de forma automatizada

with open('fichero.txt', 'r') as fichero:
    for linea in fichero:
        print(linea)
#Esto va a mostrar todas las lineas por separado