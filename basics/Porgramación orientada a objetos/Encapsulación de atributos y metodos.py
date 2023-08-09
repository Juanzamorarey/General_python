#Para acabar vamos a ver la encapsulación de atributos y métodos

#La encapsualción es una funcionalidad para impedir el acceso externo a atributos y metodos. Python hace algo parecido
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"

    def __metodo_privado(self): #Si ponemos __ delante de una función será un metodo encapsulado
        print("Soy un atributo inalcanzable desde fuera")

    def atributo_publico(self):
        return(self.__atributo_privado)#Este metodo se usa como puente para acceder a los atributos privados
    
    def metodo_publico(self):
        return(self.__metodo_privado)#Este metodo se usa como puente para acceder a la función privada

e = Ejemplo()


try:
    e.__atributo_privado #Da error y dice que no existe porque
    e.__metodo_privado #Da error porque el metodo también es privado
except:
    print("Como ves no puedes acceder a este atributo porque es privado") 

print(e.atributo_publico())
#Si llamamos al atributo que sirve de puente ya podemos acceder a dicho atributo
print(e.metodo_publico()) #Sale como código porque no hemos refefinido str pero el punto es que es accesible
