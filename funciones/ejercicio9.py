# Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

def mcm(a,b):
    if a > b:
       mayor = a
    else:
        mayor = b
    while (mayor % a !=0) or (mayor % b != 0):
        mayor +=1
    return mayor
   

print(mcm(4,6))



def mcd(a, b):

	resto = 0

	while(b > 0):

		resto = b

		b = a % b

		a = resto

	return a


print(mcd(3609,3267))