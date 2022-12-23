# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.

numero_asignaturas = int(input("¿Cuántas asignaturas tienes?"))
asignaturas = []
 
i = "pene"

for i in range(numero_asignaturas):
    i = input(str("Nombra una asignatura: "))
    asignaturas.append(i)

string_asignaturas = " ".join(asignaturas) #Esto convierte una lista en un string

print("Tienes", numero_asignaturas, "asignaturas: ", string_asignaturas)
    