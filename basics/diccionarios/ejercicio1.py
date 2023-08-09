# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.




monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}


pregunta = str(input("¿Qué símbolo de moneda quieres ver? "))


if pregunta in monedas:
    print(monedas[pregunta])
else:
    print("Esa moneda no está en el diccionario")