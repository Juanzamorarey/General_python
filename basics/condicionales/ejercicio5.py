# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales.
#  Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla 
# si el usuario tiene que tributar o no.

ingresos = float(input("¿Cuánto dinero ganas al mes?"))

edad = float(input("¿Cuántos años tienes?"))

if ingresos < 1000:
    print("No tienes que tributar")
elif edad < 16:
    print("No tienes que tributar")
else:
    print("tienes que tributar")

