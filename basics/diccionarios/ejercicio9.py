# Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
# Las facturas se almacenarán en un diccionario donde la clave de cada factura 
# será el número de factura y el valor el coste de la factura.
# El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.
# Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario.
# Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento
# y la cantidad pendiente de cobro.


catalogo_de_facturas = {}
factura_pendiente_de_pago = {}
facturas_cobradas = {}


entrada = input("Bienvenido al catálogo de facturas\n1)añadir una factura\n2)cobrar una factura\n3)salir del catálogo ")
while entrada == "1" or entrada =="2" or entrada =="3":
    if entrada == "1":
        factura_nueva = input("Introduce el nombre de la factura y el importe. Formato ejemplo (vasos:300)")
        separador_valores = factura_nueva.split(":")
        catalogo_de_facturas[separador_valores[0]] = float(separador_valores[1])
        factura_pendiente_de_pago = catalogo_de_facturas.copy()
        print("Factura añadida al catálogo")
        entrada = input("1)añadir una factura\n2)cobrar una factura\n3)salir del catálogo ")
    elif entrada == "2":
        for busca_facturas in factura_pendiente_de_pago.keys():
            busca_facturas = input("Introduce el nombre de la factura que quieres cobrar: ")
            if busca_facturas in factura_pendiente_de_pago.keys():
                valor = factura_pendiente_de_pago.get(busca_facturas)
                facturas_cobradas[busca_facturas] = valor
                del factura_pendiente_de_pago[busca_facturas]
                break
        print("Facturas que ya han sido cobradas: ",facturas_cobradas)
        print("Facturas aún por cobrar: ",factura_pendiente_de_pago)
        entrada = input("1)añadir una factura\n2)cobrar una factura\n3)salir del catálogo ")
    elif entrada == "3":
        lista_pendientes = sum(factura_pendiente_de_pago.values())
        lista_cobradas = sum(facturas_cobradas.values())
        print("La empresa tiene el siguiente balance:\n TOTAL COBRADO:{} euros\n TOTAL PENDIENTE DE COBRO:{} euros".format(round(lista_cobradas,2),round(lista_pendientes,2)))
        print("Gracias por utilizar el catálogo")
        break
    else:
        print("Eso no es una opción")
        entrada = input("1)añadir una factura\n2)cobrar una factura\n3)salir del catálogo")







    
