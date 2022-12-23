import sys
if len(sys.argv) == 3:
    texto = sys.argv[1]#Este es el pirmer argumento del script
    repeticiones = int(sys.argv[2])#Este es el segundo argumento del script
    for r in range(repeticiones):
        print(texto)
else:
    print("Faltan argumentos. Recuerda que este script tiene 3 argumentos")


# Atención los argumentos de un script se ejecutan como si fueran una lsita
# Todos los scripts necesitan tener todos los argumentos completos, si falta uno
# Dará error. Ponemos un if para evitar el error
# El señor avisa que si usas una cadena tengais cuidado porque con comillas
# simples no funciona. Usa siempre comillas dobles.
# Si el script tiene acentos o ñ debemos cambiar el tipo de codificación de ANSI a UTF-8 ya que sino dará error 
# al no reconocer la ñ o los acentos