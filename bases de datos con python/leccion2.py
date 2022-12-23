import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# Vamos a empezar con las claves primarias. Estas claves se usan como identificadores de los registros. Esta clave hará que si tenemos un registro
# unida a ella no se podrá repetir en toda la base de datos. Por ejemplo dos usuarios con el mismo dni.

# cursor.execute('''
#     CREATE TABLE usuarios (
#         dni VARCHAR(9) PRIMARY KEY,
#         nombre VARCHAR(100),
#         edad INTEGER,
#         email VARCHAR(100)
# )
# ''')

# En este código en lenguaje SQL podemos ver que aparece el PRIMARY KEY al lado del dni, esto va a hacer que no se puedan introducir dos registros con el 
# mismo dni para esta tabla. 

# usuarios = [
#     ('05438976m','Juan',27,'juanzamorarey@gmail.com'),
#     ('00000002B','Mario',51,'mario@pajillero.com'),
#     ('43829052M','luiso',32,'puto@gaylord.com'),
#     ('04853245J','Mariyinsons',67,'riguitong@putasso.com'),
# ]

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

# Introducimos ahora la lista de usuarios en la base de datos. Recordemos que este procedimiento ya se vio en la lección 1, pero ahora añadimos
# un cuarto campo a la tabla para introducir el dni. Una vez implementado esto, en el SQL browser veremos que el campo del dni tiene el icono
# de una llave, lo que nos indica que se trata de un campo de clave primaria que no se puede repetir. Si intentaramos volver a correr el programa
# daría error puesto que los usuarios ya están introducidos y no se pueden volver a introducir porque el dni se repetiría. 

# Visto lo anterior lo vamos a comentar para pasar a ver los campos autoincrementales. Estos campos asignan automáticamente un número a cada uno
# de los registros. Esto se hace para evitar tener un campo, como los dnis en el ejemplo anterior, en el que las claves tengan que ser únicas. 
# Vamos a crear un campo autoincremental. CUIDADO: PARA TRABAJAR CON ESTO SE DEBE CAMBIAR ARRIBA EL NOMBRE DE LA BASE DE DATOS A productos.db


# cursor.execute('''
#     CREATE TABLE productos (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         nombre VARCHAR(100) NOT NULL,
#         marca VARCHAR(50) NOT NULL,
#         precio FLOAT NOT NULL
#     )
#     ''')

# Aquí hemos creado una tabla productos que contiene varios campos. En el id encontramos la sintaxis para un campo autoincremental. Del mismo modo
# en el resto de campos hemos puesto NOT NULL de modo que estos campos no pueden, bajo ningún concepto, quedar vacíos. Se coemnta porque al volver a 
# crear la tabla daría error. 


productos = [
    ('champú', 'loewe',5),
    ('loción hidratante','dove',3),
    ('crema de noche','loewe',10)
]


# cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
 
# Cuando tenemos la lista de nuestros productos con todos los campos cubiertos menos el autoincremental debemos tener en cuenta que, para insertarlo
# en la tabla de la base de datos el primer valor está cubierto por el autoincremental, el cual corresponde como un argumento null. De este modo
# debemos insertar null + ?,?,?; siendo cada una de las interrogaciones uno de los campos del producto y lo primero el valor incremental. Comentamos
# para evitar errores y repeticiones en la base de datos.

# cursor.execute("SELECT *FROM productos")

# productos = cursor.fetchall()
# for producto in productos:
#     print(producto)

# Si queremos trabajar, al igual que en la leccion 1, con los productos como una lista solamente tenemos que hacer el fetchall despues de seleccionarlos.
# Comentamos para continuar después.


# Vamos a ver por última las claves únicas. El problema con las claves primarias es que no se pueden repetir campos únicos para la base de datos
# de modo que solo podemos tener un campo único. Y con el autoincremental ocurre lo mismo ya que no se pueden asignar a otro campo. Para estos casos
# usamos claves únicas, las cuales se pueden poner a pesar de que haya otros campos cuyos datos son primarios. 
# CUIDADO: CAMBIAMOS AL INICIO DE NUEVO EL NOMBRE DE LA BASE DE DATOS, AHORA ES usuarios_autoincremental. 


cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        dni VARCHAR(9) UNIQUE,
        nombre VARCHAR(100),
        edad INTEGER,
        email VARCHAR(100)
)
''')

# El atributo UNIQUE al lado del dni hace que se trate de una clave única, lo cual se suma al campo autoincremental del id dando dos campos que contienen
# claves únicas. Vamos a añadir algunos usuarios:

usuarios = [
    ('05438976m','Juan',27,'juanzamorarey@gmail.com'),
    ('00000002B','Mario',51,'mario@pajillero.com'),
    ('43829052M','luiso',32,'puto@gaylord.com'),
    ('04853245J','Mariyinsons',67,'riguitong@putasso.com'),
]

cursor.executemany("INSERT INTO usuarios VALUES (null,?,?,?,?)",usuarios)

# Ahora agregamos esta tabla a la base de datos y, si quisiéramos añadir a un nuevo usuario cuyo DNI o VALUE fuese el mismo veríamos que da error
# y no deja llevar a cabo dicha acción. Este atributo UNIQUE se puede utilizar para varios campos de modo que sean irrepetibles dentro de la misma tabla.





conexion.commit()
conexion.close()
