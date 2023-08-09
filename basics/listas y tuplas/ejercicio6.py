# Escribir un programa que almacene las asignaturas de un curso 
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, 
# pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.


lista = []

numero_asignaturas = int(input("¿cuántas asignaturas tienes?"))

for i in range(numero_asignaturas):
    nombre = input("Nombre de la asignatura: ")
    nota = int(input("Nota de la asignatura: "))
    asignatura = "Tienes que repetir la asignatura {} porque has sacado un {}".format(nombre,nota)
    lista.append(asignatura)
    if nota >= 5:
        lista.remove(asignatura) # eliminacion de elementos por valor
    else:
        pass

c = "\n".join(lista)

print(c)