import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

# En esta lección vamos a ver algunas consultas a registros específicos, modificación y borrado de registros. 

cursor.execute("SELECT * FROM usuarios WHERE id=1")
# Con este mando realizamos una consulta seleccionando todos los elementos y usando el comando WHERE que nos sirve para específicar que la id debe ser
### usuario = cursor.fetchone() 
### print(usuario)
# igual a 1. Para verlo en la consola utilizamos el ya conocido fetchone y lo imprimimos. Las búsquedas se pueden realizar siempre a través
# de campos únicos. en esta base de datos los campos únicos son el dni y el id, por lo que podríamos usar también el dni para localizar
# al usuario. 
# cursor.execute("SELECT * FROM usuarios WHERE dni='05438976m'")
# usuario = cursor.fetchone() 
# print(usuario)

# Vamos a imaginar ahora que queremos ver a todos los miembros de una base de datos que tengan 27 años. (Hemos modificado la base de datos de ejemplo
# para que Juan y Mario tengan la misma edad.) Si quisiéramos hacer esto podríamos utilizar el mismo método pero poniendo en los parámetros la edad
# y ejecutando el comando fetchall(), si utilizáramos fetchone() los usuarios con 27 años irían apareciendo uno a uno, primero Juan, luego Mario...
# cursor.execute("SELECT * FROM usuarios WHERE edad=27")
# usuarios = cursor.fetchall() 
# print(usuarios)

# Con este uso de las cláusulas Where estamos realizando consultas, pero debemos tener en cuenta que, además de las consultas podemos modificar un registro
# e incluso borrarlo. Comencemos con la modificación.

# cursor.execute("UPDATE usuarios SET nombre='Juan Zamora' WHERE dni='05438976m'")

# Aquí hemos utilizado el UPDATE y el SET para modificar un elemento en la base de datos. UPDATE modifica la tabla usuarios de modo que (SET introduce el 
# cambio) nombre pasa a ser 'Juan Zamora', cuyo dni es (WHERE) el que ya habíamos puesto antes. Esta última parte es meramente identificativa. DE modo
# que actualizamos el nombre a través de su DNI. Si Quisiéramos modificar varios campos de un mismo elemento solo tendríamos que añadir una coma tras
# el nombre y ajustar el nuevo campo

# cursor.execute("UPDATE usuarios SET nombre='Juan Zamora', edad=30 WHERE dni='05438976m'")

# Es importante señalar que si en la cláusula WHERE metiésemos una clave que afecta a varios elementos, todos ellos se verían afetados por dicha condicion.
# Del mismo modo, si no pusiéramos una cláusula WHERE lo que ocurriría sería que se modificarían todos los registros. 

# Para borrar un registro simplemente cambiamos el campo UPDATE por DELETE y SET por FROM.

cursor.execute("DELETE FROM usuarios WHERE dni ='05438976m'")
# Esto elimina al usuario con el dni ..., pero si no pusiéramos el WHERE se eliminarían todos los datos. 


conexion.commit()
conexion.close()