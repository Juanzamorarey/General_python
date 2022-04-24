#Cuando hablas de objetos tenemos que hablar también de clases, las cuales son sus moldes.


class Galleta: #Por convencion las clases empiezan por mayúscula
    pass

#Esta clase en realidad no hace nada pero podemos crear dos objetos que poseen todos los metodos internos de la clase

una_galleta = Galleta() #Así se crean los objetos, como si fuera una función
otra_galleta = Galleta()
#Este proceso se denomina instanciación. El objeto se crea en la memoria del programa pero cuando termina 
#desaparece. Es lo contrario a una base de datos o un txt

#La función type es muy útil para las clases

print(type(una_galleta))