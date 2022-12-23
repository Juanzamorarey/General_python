# Escribir un programa que lea un entero positivo, 𝑛,
# introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛. La suma de los 𝑛
# primeros enteros positivos puede ser calculada de la siguiente forma:
# suma=𝑛(𝑛+1)/2

numero = int(input("introduce un número positivo: "))

print(int(numero*((numero + 1)/2)))