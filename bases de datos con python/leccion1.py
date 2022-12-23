# El primer concepto a tener en cuenta es el acceso a la base de datos. La primera vez no existe asi que se creará automáticamente a partir de la primera entrada.
import sqlite3
# Con esto importamos el modulo

# Ahora vamos a crear la conexion a la base de datos dentro de una variable llamada conexión.

conexion = sqlite3.connect("ejemplo.db")

# En esta variable lo que hemos hecho ha sido llamar al modulo sqlite3, usar su método connect y en el argumento de la misma introducimos el nombre de la base de datos
# con la extensión db 

# Una vez esta creada la base de datos tenemos que crear una estructura principal para añadir contenido. Por ejemplo vamos a crear una tabla.
# Para ello necesitamos usar código sql. Antes de hacer esto deberemos también crear un objeto de tipo cursor.

cursor = conexion.cursor()
# Con este método ya podemos ejecutar código en formato SQL. Para ello utilizamos la variable cursor (que es un objeto) y le pasamos el metodo .execute
# con, entre paréntesis, el código SQL.

# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
# El código SQL funciona así: CREATE TABLE, crea una tabla que se llamará usuarios en este caso. Dentro del segundo paréntesis pondremos los diferentes
# campos que tendrá la tabla. EN este caso nombre tendrá un tipo de dato VARCHAR (cadena de caracteres) con un máximo de 100 caracteres por celda. El
# tipo INTEGER es para datos numéricos.

# Ahora que hemos creado esta tabla si ejecutamos 2 veces este código dará error porque ya existe dicha tabla. (Como podemos comprbar abriendo SQLite la
# base de datos de ejemplos muestra los campos y nos deja navegar por ellos, pero no tenemos nada dentro, empecemos añadiendo un registro.)
# (Vamos a comentar la ejecución de la tabla para que no dé error.)

# Vamos a insertar un registro para crear un registro en nuestra tabla de usuarios.
### cursor.execute("INSERT INTO usuarios VALUES ('Gregor',26,'greg@hotmail.com')")
# Con INSERT INTO decimos que queremos insertar en usuarios, en este caso, un nuevo valor (VALUES) que será de una cadena (''), un número y otra cadena.

# Si ejecutamos todo lo de arriba no aparecerá nada en la base de datos porque debemos confirmar los cambios que ocurran. Para ello desde la conexion
# tenemos que reafirmar con el método commit(). Esto debe hacerse justo antes de cerrar la conexion.
### conexion.commit()

# Ahora cada vez que ejecutemos el código de arriba se añadirá un nuevo elemento a nuestra base de datos. Incluso si se trata del mismo repetido. 
# Si quisieramos que no se repita habría qu ecrear un método para ello. Esto lo veremos más adelante. Vamos a intentar ahora recuperar los registros que
# están guardados en la base de datos. (Para hacer esto comentamos de nuevo lo que ya estábamos viendo antes.)

###cursor.execute("SELECT * FROM usuarios")
# Con esto estamos usando el cursor para seleccionar (SELECT) todos los campos (*) de la talba (FROM) usuarios
###print(cursor) 
# Si intentamos imprimr esto dará como resultado un bjeto ininteligible. Para poder verlo deberiamos hacer los siguiente:

###usuarios = cursor.fetchone()
# Con esta variable usamos el método fetchone() que hace que recupere el primer registro en forma de tupla, recordemos, no modificable. Pero
# Si a usuarios le asignamos un numerador similar al de las listas: [0], [1], [2]... veremos exclusivamente en campo que deseamos ver.
###print(usuarios) 
###print(usuarios[1])

# Como hemos visto hemos recuperado uno de los datos únicamente. Vamos a ver ahora como ejecutar varios registros de una sola vez. Para ello comentamos
# lo anterior.

# usuarios = [
#     ('Mario',51,'mario@pajillero.com'),
#     ('luiso',32,'puto@gaylord.com'),
#     ('Mariyinsons',67,'riguitong@putasso.com'),
# ]
# Vamos a suponer que tenemos una lista con tuplas cada una de las cuales indica el nombre, la edad y el mail de una persona. Tal y como habíamos visto antes
# pero esta vez de golpe. 

# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)
# Para introducir todos estos datos de golpe usamos el método .executemany y con una sintaxis similar insertamos en usuarios los valores con 3 interrogaciones
# puesto que son tres argumentos, y fuera del código de llamada al SQL la lista que contiene las tuplas.

# Si ahora ejecutamos el código se añadirán los tres nuevos usuarios de golpe a la base de datos. Es importante también tener en cuenta que,
# por cada vez que ejecutemos el código, se añadirán de nuevo los tres a la base de datos repitiéndose. 

# Vamos ahora a intentar recuperar varios registros de esta tabla de usuarios. (De nuevo comentamos lo anterior para seguir con la leccion)
cursor.execute("SELECT * FROM usuarios")

usuarios = cursor.fetchall()
# Con esto vamos a recuperar todos los registros que hay, en este momento, almacenados en la tabla usuarios. Este método va a recuperar los usuarios
# en un formato de lista.
print(usuarios)

# El hecho de que sea una lista nos permite trabajar con ella siguiendo los métodos acordes a la misma. Por ejemplo un bucle for que muestra
# los datos que nosotros queremos ver únicamente:
for usuario in usuarios:
    print("Nombre:",usuario[0], "Email:", usuario[2])

conexion.commit()
conexion.close()
# el método close cierra la conexion