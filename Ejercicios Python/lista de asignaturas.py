
# Este programa pregunta por una serie de asignaturas y la nota que has sacado en cada una de modo que finalmente muestra un diccionario con las asignaturas y las notas
# Proyectos y retos: Mostrar los resultados en un formato mas currado, mostrar la media del curso, mostrar en qué areas vas mejor(letras, ciencias...
# Idea: crear una gramática con un generador de palabras añadiendo listas (muy simple), despues se podrá complicar con diccionarios que incluyan aspectos semánticos



asignaturas = {}

print("Vamos a ver tus asignaturas y qué nota has sacado en cada una")

respuesta = input("¿Preparado para introducir tus asignaturas?")
while respuesta != "si":
    print("Esa respuesta no me vale")
    respuesta = input("¿Preparado para introducir tus asignaturas?")
if respuesta == "si":
        asignatura = input("Introduce una asignatura: ")
        nota = input("¿Qué nota tienes en esa asignatura?")
        asignaturas[asignatura]= str(nota)
        respuesta = input("¿Has terminado de poner todas tus asignaturas?")
        while respuesta == "no":
            asignatura = input("Introduce una asignatura: ")
            nota = input("¿Qué nota tienes en esa asignatura?")
            asignaturas[asignatura]= str(nota)
            respuesta = input("¿Has terminado de poner todas tus asignaturas?")
        while respuesta !="no" and respuesta !="si":
            print("Respuesta no válida, debes escribir si o no")
            respuesta = input("¿has terminado de poner todas tus asignaturas?")
        if respuesta == "si":
            print("Estas son todas tus asignaturas y tu nota en cada una:\n",str(asignaturas))
                




    








    




