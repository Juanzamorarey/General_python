# Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.

from math import floor

def decimal_a_binario(numero):
    numero_binario = []
    while floor(numero) >= 1:
        resultado = int(numero) % 2 
        if round(resultado) == 0:
            resultado_par = 0
            numero_binario.append(resultado_par)
            numero = numero/2
        elif resultado != 0:
            resultado_impar = 1
            numero_binario.append(resultado_impar)
            numero = numero/2
    print(numero_binario[::-1])

def binario_a_decimal(numero):
    for i in str(numero):
        list(str(numero))
        if i != "0" and i != "1":
            print("No has introducido un numero binario")
            break
    contador = 0
    i = 1
    sumador = []
    for i in list(str(numero)):
        numero_dividido = list(str(numero)[::-1])
        sumador.append(int(numero_dividido[contador])*i)
        i*2
        contador += 1
    resultado = sum(sumador)
    return(resultado)

# La primera funciona pero la segunda funcion no tira

binario_a_decimal(1110000001)