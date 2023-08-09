numero = int(input("Intoduce un número: "))

i = 0
asterisco = "*"

while i <= numero:
    i +=1
    if i <= numero:
        print(("{}".format(asterisco))*i)