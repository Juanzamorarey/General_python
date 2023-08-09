# Escribir un programa que pregunte al usuario 
# por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.


horas = input("¿Cuántas horas has trabajado?")

coste = input("¿A cuánto cobras la hora?")

total = float(horas)*float(coste)

print("te deben un total de", total, "euros")