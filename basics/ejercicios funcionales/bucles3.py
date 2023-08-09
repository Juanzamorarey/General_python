numero = int(input("Intoduce un número entero: "))

i = 0

lista = []

while i < numero:
    if i % 2 == 0:
        pass
        i +=1
    else:
        lista.append(i)
        i +=1

print(str(lista))

