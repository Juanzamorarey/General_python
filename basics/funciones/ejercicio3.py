# Escribir una función que reciba un número entero positivo y devuelva su factorial.


def factorial(numero):
    contador = 1
    for i in range(numero):
        contador *= i+1
    return contador

print(factorial(6))


