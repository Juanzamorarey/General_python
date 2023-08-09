# necesitamos un capital, un interés anual y el numero de años. Debe mostrar el capital obtenido


capital = int(input("¿Cuánto capital vas a invertir? "))

interes = int(input("¿Cuáles son los intereses? "))

años = int(input("¿Durante cuantos años? "))

beneficio_anual = (capital*(interes/100))*años


print("Con {} dinero, a un interes del {}%, durante {} años, obtienes un beneficio de {} euros.".format(capital,interes,años,beneficio_anual))