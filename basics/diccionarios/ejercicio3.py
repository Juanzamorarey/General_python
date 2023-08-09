# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Fruta 	Precio
# Plátano 	1.35
# Manzana 	0.80
# Pera 	0.85
# Naranja 	0.70



precios = {'platano':1.35, 'manzana': 0.80, 'pera': 0.85, 'naranja': 0.70}

pregunta = str(input("¿Qué fruta buscas?"))

if pregunta in precios:
    kilos = float(input("¿Cuántos kilos de fruta quieres?"))
    print("Lo que quieres comprar cuesta: ",precios[pregunta]*kilos)
else:
    print("esa fruta no la tenemos")