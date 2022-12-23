# Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y 
# muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

pregunta = input("¿Cuál es la fecha de hoy? (Formato: dd/mm/aaaa): ")

diaValue = pregunta[0:2]
mesValue = pregunta[3:5]
añoValue = pregunta[6:10]

fecha = {'diaKey':diaValue,'mesKey':mesValue,'añoKey':añoValue}

# fecha[diaKey] = int(diaValue)
# fecha[mesKey] = mesValue
# fecha[añoKey] = int(añoValue)

if int(diaValue) > 31 or int(diaValue) <=0:
    print("Eso no es posible")
elif int(mesValue) <=0 or int(mesValue) > 12:
    print("Eso no es posible")
else:
    if fecha['mesKey'] == '01':
        fecha['mesKey'] = 'enero'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '02':
        fecha['mesKey'] = 'febrero'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '03':
        fecha['mesKey'] = 'marzo'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '04':
        fecha['mesKey'] = 'abril'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '05':
        fecha['mesKey'] = 'mayo'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '06':
        fecha['mesKey'] = 'junio'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '07':
        fecha['mesKey'] = 'julio'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '08':
        fecha['mesKey'] = 'agosto'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '09':
        fecha['mesKey'] = 'septiembre'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '10':
        fecha['mesKey'] = 'octubre'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '11':
        fecha['mesKey'] = 'noviembre'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    elif fecha['mesKey'] == '12':
        fecha['mesKey'] = 'diciembre'
        print("{} de {} de {}".format(fecha['diaKey'],fecha['mesKey'],fecha['añoKey']))
    else:
        print("Error")

#Si se pone el mismo dia que mes no imprime bien porque toma el valor y lo reinterpreta con el nombre del mes para todo el diccionario
#GILIPOLLAS NO PONGAS LO MISMO PARA KEY Y PARA VALUE LERDO