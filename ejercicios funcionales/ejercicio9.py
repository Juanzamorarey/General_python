# Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

inmuebles = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
# La función recibirá como entrada la lista de inmuebles y un precio, 
# y devolverá otra lista con los inmuebles cuyo precio sea menor o igual que el dado. 
# Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario con el precio del inmueble,
#  donde el precio de un inmueble se calcula con las siguiente fórmula en función de la zona:

#     Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
#     Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5

def filtro_inmuebles (lista_inmuebles, precio):
    lista_inmuebles_con_precios = []
    for i in lista_inmuebles:
        if i['zona'] == 'A':
            if i['garaje'] == True:
                precio_final = ((i['metros']*1000) + (i['habitaciones']*5000) + 15000) * 1-(2020-i['año']/100)
                i.setdefault('precio', precio_final)
            elif i['garaje'] == False:
                precio_final = ((i['metros']*1000) + (i['habitaciones']*5000)) * 1-(2020-i['año']/100)
                i.setdefault('precio', precio_final)
        elif i['zona'] == 'B':
            if i['garaje'] == True:
                precio_final = ((i['metros']*1000) + (i['habitaciones']*5000) + 15000) * 1-((2020-i['año']/100) * 1.5)
                i.setdefault('precio', precio_final)
            elif i['garaje'] == False:
                precio_final = ((i['metros']*1000) + (i['habitaciones']*5000)) * 1-((2020-i['año']/100) * 1.5)
                i.setdefault('precio', precio_final)
        
        lista_inmuebles_con_precios.append(i)
    
    lista_inmuebles_filtrados = []
    for i in lista_inmuebles_con_precios:
        if i['precio'] <= precio:
            lista_inmuebles_filtrados. append(i)
        else:
            pass


    print("Los inmuebles disponibles para ti son:\t {}\t".format(lista_inmuebles_filtrados))


filtro_inmuebles(inmuebles,82000.20)
    


    