# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.


inversión = float(input("¿Cuánto dinero vas a invertir?"))

interés = float(input("¿Qué interés tienes?"))

years = float(input("¿Durante cuántos años?"))

resultado = float(((inversión/100)*interés)*years)

print("Vas a obtener un beneficio de: ", round(resultado,2),"euros")



