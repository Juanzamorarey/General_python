#Este curso se basa en modelos relacionales de bases de datos

#Se crean relaciones en los conjuntos de datos que tienen forma de tabla
# En este curso usaremos SQlite pero puede haber varias bases de datos que funcionens de manera diferentes


# Comenzamos importando el modulo necesario
import sqlite3
# Después creamos una conexión a la base da datos que se creara en caso de que no exista
conexion = sqlite3.connect("ejemplo.db")#COn esta variable establecemos la conexion a la base da datos
# entre paréntesis pondríamos el nombre de la base de datos que por defecto tendrá a extensión .db
cursor = conexion.cursor()
# Creamos ahora un cursor para poder operar sobre nuestra base de datos
# Para poder usar el lenguaje SQL debemos ejecutar el cursor
cursor.execute("CREATE TABLE usuarios ()")


conexion.close()#Se trata de un objeto por lo que evidentemente deberemos cerrarlo después.