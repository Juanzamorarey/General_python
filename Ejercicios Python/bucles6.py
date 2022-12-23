numero = int(input("Introduce tu numero impar: "))
i = 1
lista = []
y = 1

if i <=numero:
    if numero % 2 == 0:
        numero -1
    for i in range(numero):
        lista.insert(0,y)
        print(str(lista),"\n")
        y = y + 2
        if lista[0] == numero:
            break
        elif y > numero:
            break










#    x + (x+1)



# 1
# 3 1
# 5 3 1
# 7 5 3 1
# 9 7 5 3 1