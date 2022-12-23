contraseña = str("contraseña") 


contraseña_usuario = str(input("Dime la contraseña: "))

if contraseña_usuario == contraseña:
    print("Has introducido la contraseña: {}, y es correcta. Acceso permitido".format(contraseña_usuario))
else:
    print("La contraseña introducida es incorrecta.")