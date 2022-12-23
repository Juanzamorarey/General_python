# try:
#     n=input("Introduce un numero: ")
#     5/n
# except:
#     print("error")
    # Si ejecutamos esto normalmente no sabemos qué tipo de fallo ha ocurrido

# Para saber el tipo de error le añadimos una excepción genérica a una variable de modo que no smuestre el tipo de error

# try:
#     n=input("Introduce un numero: ")
#     5/n
# except Exception as e:
#     print(type(e).__name__)
    # Esto da como resultado el tipo de error

# Los tipos de excepciones se pueden capturar para hacer comporbaciones
# De este modo podemos adelantarnos a algunos errores que pueda cometer el usuario, por ejemplo:
# try:
#     n=input("Introduce un numero: ")
#     5/n
# except TypeError:
#     print("No se puede dividir una cadena entre un número")
    # Con esta excepción solo se leerá el código a continuación si es un typeerror

# Existen también otros tipos de errores que también se pueden captar
# ValueError -> si da error en los valores
# TypeError -> si da error en el tipo de los valores
# IndexError -> error de indexaciones
# ZeroDivisionError -> error. no se puede dividir por 0

# Usando estas excepciones podríamos cubrir todo el programa anterior de la siguiente manera
try:
    n = float(input("Introduce un numero: "))
    print(5/n)
except TypeError:
    print("No se puede dividir un número por una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir un número entre 0")
except Exception as e:
    print(type(e).__name__)
