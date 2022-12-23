from io import open
import pickle


class Pelicula:
    #Constructor de clase
    def __init__(self,titulo,duración,lanzamiento):
        self.titulo = titulo
        self.duración = duración
        self.lanzamiento = lanzamiento
        print("Se ha creado la película: ",self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

class Catalogo:

    peliculas = []

    #Constructor de clase
    def __init__(self):
        #Aquí vamos a cargar las pelícuals del fichero
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar() #añadiendo aquí guardar cada vez que agreguemos una peli se guardará

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)
        #Aquí tenemos nuestro catálogo de películas y ahora lo que vamos a hacer es guardar y cargar los datos dentro de un fichero
        #Para que no se borre nuestro catálogo cada vez que lo cerramos       
    def cargar(self):#Esto cargará el contenido del fichero
        fichero = open('catálogo.pckl','ab+')#Append binario con + que indica lectura
        fichero.seek(0) #Debido al modo append el puntero se iniciará siempre al final y no podremos leer. Por eso recolocamos el puntero
        try:
            self.peliculas = pickle.load(fichero)
            #Debido a que la primera vez no va a existir el fichero dará el error y entonces se implementará desde el except
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()#Cerramos siemrpe el fichero
            print("Se han cargado {} películas".format(len(self.peliculas)))
    def guardar(self):#Esto guardará el contenido del fichero
        #Aquí vamos a abrir el fichero en escritura binaria eliminando los datos, añadiendo los nuevos y volcando de nuevo el fichero
        fichero = open('catálogo.pckl','wb')
        pickle.dump(self.peliculas, fichero)#volcamos la lista de peliculas en el fichero
        fichero.close()
        #La siguiente función de la clase es una prueba, aún debe realizarse
    def eliminar(self,pelicula_eliminada): #NO FUNCIONA
        if pelicula_eliminada in self.peliculas:
            self.peliculas.remove(pelicula_eliminada)
            print("La película {} ha sido eliminada".format(pelicula_eliminada))
            self.guardar()
        else:
            print("Esa película no está en el catálogo")   
    #Destructor de clase
    def __del__(self):
        self.guardar() #Esto guardaría automáticamente los datos en caso de que cerremos el programa sin guardar previamente
        print("Se ha guardado el fichero")

# c = Catalogo()
# c.agregar(Pelicula("El padrino",175,1972))
# c.agregar(Pelicula("El Padrino II",202,1974))
# c.mostrar()
# del(c)
# c.agregar (Pelicula ("regueton duro", 123, 1987))
#(Debemos tener cuidado al ejecutar estos comandos porque el código es recursivo, es decir
# si ejecutamos el código varias veces pueden ocurrir errores ya que la información se ha guardado y no se borra con el código sino cuando eliminamos el archivo)
c = Catalogo()
c.agregar(Pelicula("El padrino",175,1972))
c.agregar(Pelicula("El Padrino II",202,1974))
c.eliminar("El padrino")
c.mostrar()
