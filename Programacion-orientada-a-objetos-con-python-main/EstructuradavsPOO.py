#Vamos a hablar de la programación orientada a objetos

# Definimos unos cuantos clientes
clientes= [
    {'Nombre': 'Hector', 'Apellidos':'Costa Guzman', 'dni':'11111111A'},
    {'Nombre': 'Juan', 'Apellidos':'González Márquez', 'dni':'22222222B'} 
]

# Creamos una función que muestra un cliente en una lista a partir del DNI
def mostrar_cliente(clientes, dni):
    for cliente in clientes:
        if (dni == cliente['dni']):
            print('{} {}'.format(cliente['Nombre'],cliente['Apellidos']))
            return
    print('Cliente no encontrado')

# mostrar_cliente(clientes, '11111111A')

def borrar_cliente(clientes, dni):
    for i,c in enumerate(clientes): #La i es el índice mientras que el c es el iterador
        if (dni == c['dni']):
            del( clientes[i] ) #Se slimina por el índice por eso funciona el metodo del que va con listas
            print(str(c),"> BORRADO")
            return

    print('Cliente no encontrado')

#Este sería el ejemplo de programación estructurada Vamos a ver el ejemplo con programación orientada a objetos

class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)

# Y otra para las empresas
class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

### Ahora utilizaré ambas estructuras

#La programación orientada a objetos (POO) se basa en determinar las entidades con nombre propio en lugar de crear estructuras para representar
#la información. Cada entidad tendrá sus variables internas y sus funcionalidades internas. Cada entidad es un objeto