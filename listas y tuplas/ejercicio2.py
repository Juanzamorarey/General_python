# Escribir un programa que almacene las asignaturas de un curso 
# por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje
# Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

eleccion = int(input(
    "¿Qué asignatura estudias: \n 1. Matemáticas \n 2. Física \n 3. Química \n 4.Historia \n 5.Lengua \n"
))

if eleccion == 1:
    print("Yo estudio", lista[0])
elif eleccion == 2: 
    print("Yo estudio", lista[1])
elif eleccion == 3: 
    print("Yo estudio", lista[2])
elif eleccion == 4: 
    print("Yo estudio", lista[3])
elif eleccion == 5: 
    print("Yo estudio", lista[4])
else:
    print("Esa asignatura no está disponible")