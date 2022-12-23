# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y 
# después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas
# de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.


lista_asignaturas = []

numero_asignaturas = int(input("¿Cuántas asignaturas tienes?"))

for i in range(numero_asignaturas):
    nombre = str(input("¿Cómo se llama esa asignatura?"))
    nota = float(input("¿Qué nota tienes en esta asignatura?"))
    nom_not = "En {} has sacado un: {} \n".format(nombre,nota)
    lista_asignaturas.append(nom_not)

a = " ".join(lista_asignaturas)

print(a)



