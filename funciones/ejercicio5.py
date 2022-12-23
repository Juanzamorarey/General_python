# Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.


def calcular_area_circulo(radio):
    resultado = 3.14*(radio**2)
    return resultado

def calcular_volumen_cilindro(calcular_area_circulo, altura):
    volumen = calcular_area_circulo*altura
    return volumen


print(calcular_volumen_cilindro(calcular_area_circulo(6),8),"cm cúbicos")