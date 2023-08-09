# Para trabajar con excepciones tenemos que tener en cuenta el tipo de error.
# EN la practica vamos a poner un bloque de código dentro de un try: y si no funciona estableceremos otro bloque except: que se ejecutará si ocurre un erroe en el primero

# try:
#     n = float(input("introduce un numero: "))
#     m = 4
#     print("{}/{}={}".format(n,m,n/m))
# except:
#     print("Ha ocurrido un error. Quizá has introducido una cadena y no un numero")

# En este ejemplo, si el usuario introdujera una cadea en el input en vez de detenerse la ejecución del programa se pasaría
# al bloque de código de excepción. mostrando el mensaje de except.

# Si quisieramos que el usuario siguiera intentándolo hasta que lo hiciera correctamente podriamos introducir todo el programa
# dentro de un bloque while. PERO SI HACEMOS ESTO ES IMPORTANTE RECORDAR ROMPER LA ITERACIÓN.
while(True):
    try:
        n = float(input("introduce un numero: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        # break
    except:
        print("Ha ocurrido un error. Quizá has introducido una cadena y no un numero")
    else:
        print("Todo ha ido bien")
        # Si introducimo sun else podemos asegurarnos de que todo el programa ha funcionado correctamente
        break #Si hacemos esto debemos situar aquí el fin de la iteración
    finally:
        print("fin de la iteración")
        # Con el finally lo que hacemos es mostrar un mensaje ocurra o no un error