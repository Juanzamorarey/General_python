# Vamos a crear un a aplicación sencilla de web_scrapping para ver cuál es el lenguaje
# más utilizado actualmente. Para ello seguiremos la siguienteestructura:

# 1o ----> Nuestro script de python hace un request a la URL https://news.ycombinator.com/news
# 2o ----> Recibimos un RAW DATA de la llamada que deberemos parsear con beatiful soup
# 3o ---->  procesaremos estos datos con pandas y los visualizaremos con matplotlib

# IMPORTANTE: hay que tener cuidado con lo que se hace web_scrapping peusto que se puede sobrecargar el servidor
#Documentacion de beatiful_soup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def main():
    url = "https://news.ycombinator.com/item?id=29782099"
    # Para llevar a cabo el web scrapping usaremos .get() de la libreria requests
    respuesta = requests.get(url)
    # Veamos como se ve la respuesta

    # print(respuesta)

    # Así solo veremos el objeto, para ver el contenido deberemos hacer un . content

    # print(respuesta.content)

    # Como vemos la respuesta es un gran html, ahora tenemos el raw data pero necesitamos limpiarlo,
    # Para ello vamos a usar BeautifulSoup, una libreria bastante popular
    soup = BeautifulSoup(respuesta.content, "html.parser")
    # Para que BeatifulSoup funcione debemos indicarle qué lenguaje debe parsear, en este casoratian
    # y en la mayoria de casos de datos de internet los esqueletos están hehcos con html asi que utilizaremos
    # este parseador pasandolo como otro argumetno
    # Es por tanto relevante que primero veamos con el inspector la página a la que vamos a hacer
    # web_scrapping para identificar si hay posibles clases o etiquetas que se repiten y que queremos rescatar
    #Imaginemos que para este tutorial queremos rescatar los comentarios de los usuarios. COmo se ve
    #facilmente hay una etiqueta div con una clase llamada comment <div class="comment">. EL problema que vemos es que
    # esta etiqeuta se utiliza tambiémn para las respuestas a los comentarios que, imaginemos, no queremos. 
    #Por ahora empecemos extrayendo la parte que nos interesa.

    #La manera de hacer esto con BeatifulSoup es exremadamente sencilla:

    # elementos = soup.find_all(class_="comment")

    # Tenemos que usar el _ en class porque en python se trata de una palabra reservada.
    #Esta función nos va a devoler una lista de elementos

    # print(f"Numero de elementos: {len(elementos)}" )

    #Contamos con 250 elementos en total. Son demasiados por lo que tendremos que filtrar quitando los
    #subcomentarios, para ello debemos ver a nivel de estructura como filtrar esos subcomentarios. COmo vemos
    #los comentarios están identados, vamos a iintentar buscar esa identación en nuestra llamada para ver
    #si podemos identificar las respuestas y eliminarlas. 
    #Mirando con el inspector vemos que existe una clase llamada "ind" cuyo nivel de identacion es 1 mientras
    # que en los comentarios principales el nivel de identaci´pon es 0. Podemos por tanto mirar esta identación
    #y una vez la hayamos identificado buscar el siguiente div de la clase comment y extraerlo.
    #  Vamos a filtrar por tanto a partir de este dato, intentamoslo de nuevo

    elementos = soup.find_all(class_="ind", indent=0)
    #Buscamos el class ind con indent 0 
    # En la documentacion vemos el metodo find_all_next() que devuelve todos los matches
    #y find_next() que devolverá solo el primer match. En nuestro caso queremos el primero
    #Veamos como se implementa en una lista de comprensión

    comentarios = [elemento.find_next(class_ ="comment") for elemento in elementos]

    #Por lo tanto comentarios es una lista resultante de iterar un elemento que
    #busca el siguiente elemento llamado comment de los indice en la lista elementos

    # print(f"Comentarios: {len(comentarios)}")
    # print(f"Comentarios: {comentarios[0]}")

    #Como vemos ahora tenemos 84 comentarios, por lo que al eliminar respuestas hemos pasado de 250 a
    #84 y podemos ver el primer comentario pero sigue teniendo todas las etiquetas molestas.
    # Vamos a usar la función get_text() para asegurarnos de que recuperamos solo el texto

    # print(f"Comentario limpio: {comentarios[0].get_text()}")
    #Como podemos ver ahora sí que extrae el comentario tal cual lo queremos

    #Imaginemos que en estos comentarios estuviéramos ahora interesados en ver qué lenguajes de programación
    #se utilizan. Para ello deberemos escanear cada comentario y contar el número de ocurrencias de cada
    #lenguaje. Pero cuidado, si el mismo lenguaje aparece 2 o más veces en un comentario debe contar únicmente
    #como una sola vez. 
    #Debemos entonces determinar qué keywords vamos a buscar y normalizar también el texo eliminando stop_words 
    # y normalizando a minúsculas. 

    keywords = {
        "python": 0,
        "javascript": 0,
        "typescript": 0,
        "ruby": 0,
        "java": 0,
        "rust": 0,
        "c#": 0,
    }

    #Estas van a ser nuestras keywords emepcemos por hacer un bucle que cambie los comentarios a lower_case

    # for comentario in comentarios:
    #     texto_comentario = comentario.get_text().lower()
    #     palabras_comentario = texto_comentario.split(" ")
    #     print(palabras_comentario)

    #Como vemos aquí encontramos diferentes tokens que tienen ruido del tipo signos de puntuación,
    #o palabras repetidas. Tenemos que limpiar un poco mas para ello usaremos la funcion strip()

    # for comentario in comentarios:
    #     texto_comentario = comentario.get_text().lower()
    #     palabras_comentario = texto_comentario.split(" ")
    #     palabras_comentario = [palabra.strip(".,/:;!@") for palabra in palabras_comentario]
    #     print(palabras_comentario)

    #Aunque hemos limpiado bastante necesitamos poder visualizar de un solo vistazo
    #nuestros datos. Para ello podemos convertir estas palabras en un set o diccionario y
    #dado que no vamos a necesitar el value, usaremos un set. Para hacerlo con listas de comprensión
    # solo debemos cambiar [] por {} y veremos como cambia a un set. Prbemos

    for comentario in comentarios:
        texto_comentario = comentario.get_text().lower()
        palabras_comentario = texto_comentario.split(" ")
        palabras_comentario = {palabra.strip(".,/:;!@") for palabra in palabras_comentario}
        # print(palabras_comentario)
        for k in keywords:
            if k in palabras_comentario:
                keywords[k]+=1

    print(keywords)
    #Gracias que se trata de un set no tendremos valores duplicados. Por lo tanto ahora podremos iterar
    #sobre nuestro diccionario y,en caso de que se muestre la palabra, sumaremos uno a sus valores.
    #Recordemos que comentarios contiene una lista con los comentarios separados por lo que 
    #solo se contará 1 vez por cada comentario en el que aparezca.


    #Si bien la parte central del script ya está terminada, siempre queda mejor visualizar los datos
    #en un gráfico,para ello utilizaremos matplotlib. Lo importamos y llamamos al metodo

    plt.bar(keywords.keys(), keywords.values())
    plt.xlabel("Lenguaje de programación")
    plt.ylabel("Ocurrencias")
    plt.show()


    #El pimer argumento estará en el eje de las x y en el segundo el eje de las y. También podemos añadir
    #Visualizaciones 


        

    

if __name__ == "__main__":
    main()