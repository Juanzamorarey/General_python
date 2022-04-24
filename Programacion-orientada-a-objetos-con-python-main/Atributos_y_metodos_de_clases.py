class Galleta():
    pass

una_galleta = Galleta()
#Aquí creamos un objeto
una_galleta.sabor = "salado"
una_galleta.color = "marrón"
#Aquí le añadimos atributos

#Cada objeto puede tener sus propios atributos de tal manera que, si este no existe dentro del objeto se creará
#automáticamente y podremos utilizarlo

print(f"El sabor de esta galleta es {una_galleta.sabor} "
      f"y el color {una_galleta.color}")

#Los atributos se pueden definir dentro de la clase de modo que no haya que irlo especificando en cada uno de los 
#objetos sino que vengan por defecto

class Galleta_con_atributos():
    chocolate = False

galleta_atributada = Galleta_con_atributos()#Creamos la galleta con atributo
print(galleta_atributada.chocolate) #Esto dará False porque las galletas no tienen chocolate pero vamos a cambiarlo

galleta_atributada.chocolate = True
print(galleta_atributada.chocolate) #Ahora el chocolate es True


#Para continuar vamos a explicar el metodo __init__ y la palabra reservada self

class Galleta_con_metodo():
    chocolate = False
    def __init__(self):#El metodo init es un metodo especial que se ejectua al crear un objeto, permite enviar 
                        #Argumentos durante la instanciación. La palabra self sirve para diferenciar entre el 
                        #ámbito de clase y el del metodo, es un requisito implícito en el metodo.
        print("Se acaba de crear una galleta")

galleta_metodica = Galleta_con_metodo()

#Vamos a ver ahora una clase con un metodo interno propio que puede cambiar el valor del atributo chocolate

class Galleta_con_metodo_propio():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta")
    
    def chocolatear(self):
        chocolate = True #Si escribimos esto estamos hablando de una variable única dentro de la función que está dentro del método
        #Para que funcione de manera general para el objeto generado por esta clase debemos usar la palabra self
        self.chocolate = True #Este si va a funcioanr porque cambiar el atributo interno de la galleta general a True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada")
        else:
            print("Soy una galleta sin chocolate")

galleta_propia = Galleta_con_metodo_propio() #Creamos una galleta
galleta_propia.tiene_chocolate() #Comprobamos si tiene chocolate


galleta_propia.chocolatear() #Llamamos al metodo que cambia el valor de chocolate a True
galleta_propia.tiene_chocolate() #Comprobamos si tiene chocolate



#Vamos a ver ahora como crear un metodo en el que se van a introducir atributos por defecto para los objetos de una clase
class Galleta_con_metodos_iniciales():
    chocolate = False
    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        #Lo que hacemos aquí es asignar a todos los objetos creados con esta clase el requerimiento de unos
        #"atributos". Estos atributos los definiremos a la hora de crear el objeto pero en la propia clase
        #necesitamos la palabra self para definirlos. Así si yo ahora hago esto 
        #Galleta_con_metodos_iniciales("salado","marrón")
        #Estoy asignando directamente a los atributos sabor y color el valor de los argumentos que he pasado
        #al crear el objeto.
        print(f"Se acaba de crear una galleta {sabor} y {color}")
    def chocolatear(self):
        chocolate = True #Si escribimos esto estamos hablando de una variable única dentro de la función que está dentro del método
        #Para que funcione de manera general para el objeto generado por esta clase debemos usar la palabra self
        self.chocolate = True #Este si va a funcioanr porque cambiar el atributo interno de la galleta general a True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada")
        else:
            print("Soy una galleta sin chocolate")

galleta_inicial = Galleta_con_metodos_iniciales("salada","marrón")
#Si llamaramos a esta clase sin pasarle los argumentos iniciales de su metodo __init__ daría error.
#Para evitar esto podríamos definir un valor por defecto en el propio __init__
class Galleta_con_metodos_iniciales_y_valores_por_defecto():
    chocolate = False
    def __init__(self, sabor=None, color=None):#Esta clase se puede llamar sin argumentos porque no dará error
                                                #Sabor y color tendrán el valor None
        self.sabor = sabor
        self.color = color
        print(f"Se acaba de crear una galleta {sabor} y {color}") #sabor y color tienen el valor NONE

        
galleta_inicial_fea = Galleta_con_metodos_iniciales_y_valores_por_defecto()