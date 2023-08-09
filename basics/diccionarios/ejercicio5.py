# Escribir un programa que almacene el diccionario con los 
# créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre 
# por pantalla los créditos de cada asignatura en el formato 
# <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos
# Al final debe mostrar también el número total de créditos del curso.

asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}

claves = list(asignaturas.keys())
valores = list(asignaturas.values())

print("Tus asignaturas son:\n{}: tiene {} créditos\n{}: tiene {} créditos\n{}: tiene {} créditos\n".format(claves[0],valores[0],claves[1],valores[1],claves[2],valores[2]))
print("El total de créditos es: {}".format(sum(valores)))

#Métodos útiles: .keys() saca las claves de un diccionario, para convertir las claves en una lista con list(diccionario.keys())
#Métodos útiles: .values() saca los valores de un diccionario, para convertir los valores en una lista con list(diccionario.values())
#Metodos útiles: sum(lista) realiza la suma de todos los valores de una lista con números.