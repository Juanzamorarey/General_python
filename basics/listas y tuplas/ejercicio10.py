# Escribir un programa que almacene en una lista los siguientes precios
#, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

lista_precios = [50,75,46,22,80,65,8]

y = 0

# for i in lista_precios:
#     while y not in lista_precios:
#         y += 1
#     else:
#         print("El numero mas bajo es : {}".format(y))
#         break
#  esto era la manera complicada pero existen los metodos de mas abajo para solucionar el problema

for i in lista_precios:
    print("El numero mas bajo es: {}".format(min(lista_precios)))
    break

for i in lista_precios:
    print("El numero mas alto es :",max(lista_precios))
    break
   
