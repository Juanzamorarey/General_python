# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad = float(input("Introduce la cantidad de dinero a invertir: "))

interes = float(input("Introduce el porcentaje anual de interés: "))

tiempo = int(input("Introduce los años: "))

for i in range(tiempo):
    cantidad *= 1 + interes/100
    print("En el año", str(i+1),"Se ha obtenido un beneficio de ", i, "que suma un total de: ", round(cantidad))

#No lo he sacado yo