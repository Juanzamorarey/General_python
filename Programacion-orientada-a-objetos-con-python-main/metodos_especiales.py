#Vamos a ver algunos metodos especiales de cada una de las clases

class Pelicula:

    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print(f"Se ha creado la pelicula {titulo}")

    #Destructor de clase
    def __del__(self):
        print(f"Se está borrando la pelicula {self.titulo}")#Cuidado, si solo pones titulo es la funcion y queremos el objeto de la clase

    #El metodo destructor se ejecuta automáticamente al final del programa para borrar los datos que no se van a reutilizar del programa 
    #Un problema habitual de las clases es que al imprimir un objeto no sale lo que deseamos, para ello debemos reasignar
    #su propio metodo string interno. 
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)

    #Otro metodo útil es el len para, por ejemplo, ver la longitud de una pelicula. Los metodos habituales no están
    # implementados en los objetos
    def __len__(self):
        return self.duracion




peli = Pelicula("Lola",123,1965)
# del(peli)
print(str(peli))
print(len(peli))