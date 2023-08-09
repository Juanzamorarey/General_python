# Escribir un programa que cree un diccionario simulando una cesta de la compra.
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
# hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total,
# con el siguiente formato
# Lista de la compra 	 
# Artículo 1 	Precio
# Artículo 2 	Precio
# Artículo 3 	Precio
# … 	…
# Total 	Coste


cesta_compra = {}

artículos = {'patatas': 0.80, 'pimientos': 1.00, 'tomates': 1.20}

respuesta = input(
    "Estás en una frutería con patatas, pimientos y tomates.\n Estos son los precios:\n patatas:0.80\npimientos:1.00\ntomates:1.20\n ¿Qué quieres comprar?"
    )
while respuesta == "patatas" or respuesta == "tomates" or respuesta == "pimientos":
    if respuesta == "tomates":
        kilos_tomates = int(input("¿Cuántos quieres?"))
        cesta_compra.setdefault('tomates',round(kilos_tomates*1.20,2))
        print("Se han añadido {} tomates a la cesta de la compra".format(kilos_tomates))
        comprar_mas = input("¿Quieres algo más?")
        if comprar_mas == "no":
            break
        if comprar_mas == "si":
            respuesta = input(
            "Estás en una frutería con patatas, pimientos y tomates.\n Estos son los precios:\n patatas:0.80\npimientos:1.00\ntomates:1.20\n ¿Qué quieres comprar?"
            )
    elif respuesta == "pimientos":
        kilos_pimientos = int(input("¿Cuántos quieres?"))
        cesta_compra.setdefault('pimientos',kilos_pimientos*1.00)
        print("Se han añadido {} pimientos a la cesta de la compra".format(kilos_pimientos))
        comprar_mas = input("¿Quieres algo más?")
        if comprar_mas == "no":
            break
        if comprar_mas == "si":
            respuesta = input(
            "Estás en una frutería con patatas, pimientos y tomates.\n Estos son los precios:\n patatas:0.80\npimientos:1.00\ntomates:1.20\n ¿Qué quieres comprar?"
            )
    elif respuesta == "patatas":
        kilos_patatas = int(input("¿Cuántas quieres?"))
        cesta_compra.setdefault('patatas',round(kilos_patatas*0.80,2))
        print("Se han añadido {} patatas a la cesta de la compra".format(kilos_patatas))
        comprar_mas = input("¿Quieres algo más?")
        if comprar_mas == "no":
            break
        if comprar_mas == "si":
            respuesta = input(
            "Estás en una frutería con patatas, pimientos y tomates.\n Estos son los precios:\n patatas:0.80\npimientos:1.00\ntomates:1.20\n ¿Qué quieres comprar?")
else:
    print("De eso no tenemos")

claves = list(cesta_compra.keys())
valores = list(cesta_compra.values())

print("Tu lista final de la compra es:\n")
for i in cesta_compra:
    i = 0
    while i < len(cesta_compra):
        print("{}: {} euros".format(claves[i],valores[i]))
        i +=1
    else:  
        break