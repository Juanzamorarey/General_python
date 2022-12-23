# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
# Después el programa debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

barra_pan_dia = 3.49

barras_vendidas = int(input("¿Cuántas barras, que no son del día, se han vendido?"))

beneficio = barras_vendidas*(barra_pan_dia*0.60)

print("Normalmente una barra vale", barra_pan_dia,"pero, al no ser del día se descuenta el 60%. En total hemos ganado",round(beneficio,2),"con las barras duras")
