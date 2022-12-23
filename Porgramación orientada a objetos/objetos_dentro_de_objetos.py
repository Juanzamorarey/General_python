#Vamos a ver la posibilidad de utilizar objetos dentro de objetos
class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", 175, 1972) #Aquí creamos la película desde la clase película
peli = Pelicula("Lola",123,1965)
c = Catalogo([p,peli])  # Añado una lista con una película desde el principio
c.mostrar()
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))  # Aquí sin embargo utilizando el metodo agregar
                                                        # del catalogo agregamos directamente un objeto pelicula
                                                        #  el cual creamos dentro de los paréntesis del mismo metodo
                                                        #  agregar
c.mostrar()