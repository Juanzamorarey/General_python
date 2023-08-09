# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones.
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra.
# Si una palabra no está en el diccionario debe dejarla sin traducir.


diccionario = {}

pregunta_inicial = input("¿Quieres usar el diccionario? ")
while pregunta_inicial == "si":
    pregunta = input("¿Quieres añadir una nueva equivalencia al diccionario (1) o traducir una frase(2)?: ")
    if pregunta == "1":
        entrada_diccionario = input("Introduce la equivalencia. (Formato ejemplo -> libro:book): ")
        separador_español_ingles = entrada_diccionario.split(":")
        diccionario[separador_español_ingles[0]] = separador_español_ingles[1]
        print(diccionario)
        pregunta_inicial = input("¿Quieres usar el diccionario? ")
    elif pregunta == "2":
        frase = input("Introduce la frase que quieres traducir: ")
        palabras_frase = list(frase.split(" ")) #Lista de las palabras en la frase
        palabras_en_diccionario = diccionario.keys() #Lista de las palabras definidas en el diccionario
        for palabra_a_traducir in palabras_frase: #Para palabra_a_traducir en la lista de palabras de la frase
            if palabra_a_traducir in palabras_en_diccionario: #Si la palabra está en el diccionario
                término = diccionario[palabra_a_traducir] #término es la palabra traducida. Traduce la palabra y llámaña término
                posicion_de_la_palabra = palabras_frase.index(palabra_a_traducir) #la posición de la palabra traducida en la frase
                palabras_frase[posicion_de_la_palabra] = término #en la lista de palabras de la frase cambiamos la palabra en español por la palabra en inglés
                frase_traducida = " ".join(palabras_frase)
        print(frase_traducida)
        pregunta_inicial = input("¿Quieres usar el diccionario? ")
    else:
        print("Lo siento, no te entiendo")
else:
    print("adios")


