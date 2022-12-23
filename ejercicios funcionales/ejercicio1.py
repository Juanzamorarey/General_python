# Escribir una funcion que aplique un descuento y otra que aplique el iva. Una tercera función debe recibir un diccionario
#  con los precios y porcentajes de una cesta de la compra y una de las funciones anteriores y utilice la función pasada para aplicar los descuentos
# o el Iva a los productos de una cesta y devolver el precio final de la cesta. 


def descuento(precio, porcentaje):
    dinero_descontado = float(precio)*(porcentaje/100)
    return float(dinero_descontado)


# descuento(100)



def iva (precio):
    iva_del_producto = precio*0.21
    return float (iva_del_producto)


# iva(100)

mi_lista_compra = {'descuentos': [15,30,5], 'precios':[75,20,15]}
# 90 + 18,9
# 80 + 16,8
# 70 + 14,7

# 290,4
lista_articulos = []


def funcion_ejercicio(lista_compra):
    precios = lista_compra['precios'] 
    porcentajes = lista_compra['descuentos']
    
    for i in range(0, len(precios)):
        descuento_sobre_producto = descuento(precios[i],porcentajes[i])
        producto_con_descuento = precios[i] - descuento_sobre_producto
        iva_articulo = iva(producto_con_descuento)
        articulo_final = producto_con_descuento + iva_articulo
        lista_articulos.append(articulo_final)
        i += 1

    print(sum(lista_articulos))



funcion_ejercicio(mi_lista_compra)


# Cosas a tener en cuenta en el ejercicio:

# 1. Para convertir los elementos de un diccionario en una lista debes establecer la clave a la que van asociados los valores: nombre_diccionario['clave']

# 2. En un bucle for para recorrerlo sin poner la i = 0 que trastoca los planes de recorrer la lista hay que poner un range. Este range tiene 2 argumentos
# el primero será un 0 (la posición desde donde empieza a iterar), el segundo será el len(lista), si queremos que recorra toda la lista o la posición donde
# queramos que pare. 


   