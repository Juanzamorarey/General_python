class Asignaturas():
    def __init__(self,nombre=None,nota=None,rama=None):
        self.nombre = nombre
        self.nota = nota
        self.rama = rama

    def __str__(self):
        imprimir = "Asignatura: {} \nNota: {} \nRama {}".format(self.nombre,self.nota,self.rama)
        return imprimir

    def media_curso(self, lista):
        asignaturas = len(lista)
        media_asignatura = self.nota/len(lista)
        suma = 0
        suma + media_asignatura
        for i in lista:
            media_asignatura = i.self.nota/(len(lista))
            suma = 0
            suma + media_asignatura
        if i == asignaturas:
            print(suma)
        





matematicas = Asignaturas("matematicas",5,"ciencias")
fisica = Asignaturas("fisica",6,"ciencias")
quimica = Asignaturas("quimica",8,"ciencias")


lengua = Asignaturas("lengua",8,"letras")
historia = Asignaturas("historia",7,"letras")
filosofía = Asignaturas("filosofía",5,"letras")

asignaturas = []

asignaturas.append(str(matematicas))
asignaturas.append(str(fisica))
asignaturas.append(str(quimica))
asignaturas.append(str(lengua))
asignaturas.append(str(historia))
asignaturas.append(str(filosofía))

for i in asignaturas:
    print(i,"\n")

i = 0
while i < len(asignaturas):
    i + 1
    for h in asignaturas:
        suma = 0
        media_asignatura = h.media_asignatura(asignaturas)
        suma + media_asignatura
if i == len(asignaturas):
    print("Esta es tu media: ",suma)



        




