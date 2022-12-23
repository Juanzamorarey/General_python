# Escribir una función reciba una lista de notas y devuelva la lista de calificaciones correspondientes a esas notas.

def calificador (lista):
    lista_calificaciones = []
    print("Tus calificaciones son: \t")
    for i in lista:
        if i <= 4:
            lista_calificaciones.append("insuficiente")
        elif i == 5 or i ==6:
            lista_calificaciones.append("suficiente")
        elif i== 7 or i ==8:
            lista_calificaciones.append("notable")
        elif i==9 or i ==10:
            lista_calificaciones.append("sobresaliente")
        else:
            lista_calificaciones.append("nota no computable")
    for notas in zip(lista,lista_calificaciones):
        print(notas)


mis_notas = [3,5,8,4,9,10,5,7,3,10]

calificador(mis_notas)