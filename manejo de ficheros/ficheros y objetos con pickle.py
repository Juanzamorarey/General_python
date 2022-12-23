from io import open

# Vamos a usar el modulo pickle para trabajar con ficheros binarios
import pickle #Esta librería es la mejor para trabajar con objetos

lista = [1,2,3,4,5]

fichero = open('lista.pckl','wb')
# Es importante recordar que la extensión no es importante, así que lo llamamos así para recordar que es pickle
# Si es importante en cambio el modo de 'wb' ya que indica escritura binaria
# Tiene las mismas peculiaridades, al ser el modo write te machaca el docuemnto

pickle.dump(lista,fichero)#Este metodo borra lo que hay en el fichero e incorpora el argumento que se le pase en el fichero (2o argumento)
fichero.close()
#Ahora mismo no se puede leer el archivo porque está en binario
# Para recueprar la estructura de este fichero binario leemos en lectura binaria con puntero al pirncipio
# Como nosotros sabemos que tenemos una lista usamos el metodo pickle.load()

fichero = open('lista.pckl','rb')
lista = pickle.load(fichero)#Con este metodo cargamos la lista
print(lista)
# De nuevo debemos tener en cuenta que después de load el puntero está al final por lo que estamo sla final del contenido
# Si queremos volver a cargar el contenido debemos mover el puntero al inicio de nuevo
fichero.seek(0)#recolocamos el puntero al princpio
lista = pickle.load(fichero)
print(lista)

# (Por lo tanto para trabajar con pickle lo que debemos hacer es lo siguiente:
# primero: crear una colección, algo, unos datos que almacenar, listas, objetos, diccionarios...
# segundo: volcar dentro del fichero binario con el metodo .dump()
# Desde fuera no se podrá ver porque serán datos binarios pero sabemos lo que es desde el código
# último: recuperar los datos con el método load() en modo lectura )
#Se recomienda anotar qué tipo de datos son con un comentario

#Vamos a crear ahora unos objetos y almacenarlos en un fichero:
class Persona:

    def __init__(self,nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

#Hemos creado una clase que crea objetos personas

nombres = ["Hector","Mario","Marta"]
personas = []
for n in nombres:
    p = Persona(n)
    personas.append(p)

#A una lista le agregamos los objetos de forma dinámica

fichero = open('personas.pckl','wb')
pickle.dump(personas,fichero)

#Y los añadimos en binario. Ahora tenemos que recuperarlos antes de poder verlos en el fichero

fichero = open('personas.pckl','rb')
personas = pickle.load(fichero)
fichero.close()
#Aquí lo hemos recuperado de modo que le siguiente for deberia funcionar

for p in personas:
    print(p)
