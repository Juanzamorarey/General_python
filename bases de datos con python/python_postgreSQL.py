import psycopg2

# Vamos a crear un ejemplo sencillo en el que almacenamos en una BBDD los clientes y las reservas de un hotel. 


# Master password: Pepetijuelasnaciel28
# Para acceder al conjunto de servidores que tienes
# Contraseña: Pepetijuelas28
# Para acceder a una BBDD concreta
# En postgress todas las BBDD se manejan por esquemas
# Dentro de estos schemas estarán las tablas. 
# Para visualizar las tablas se puede dar clic derecho sobre ellas y usar view, eligiendo una
# configuración que queramos (100 filas, 50 filas..)
# #

# Para conectarnos a una BBDD de postgre utilizando psycog2 podemos hacerlo de esta forma:

# conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")

# cursor = conexion_BBDD.cursor()

# # Algunas funciones básicas de uso:
#  .cursor() crea un cursor para moverse por la BBDD
#  .execute() ejecuta la orden que le vamos a dar a la BBDD. 
#  .commit() commitea los cambios a la BBDD.
#  .close() cierra la conexion con la BBDD.
# .fetchall() devuelve todas las filas de una tabla
# .fetchone() devuelve una fila concreta
# .fetchmany(SIZE) devuelve un número limitado de filas
# 
# cursor.execute("CREATE TABLE Clientes (idCliente INT PRIMARY KEY, Nombre VARCHAR(20),Edad INT, Telefono INT, Correo VARCHAR(50))")
# cursor.execute("CREATE TABLE Reservas (idReserva INT PRIMARY KEY, idCliente INT, Nombre VARCHAR(20),fecha_inicio VARCHAR(11), fecha_fin VARCHAR(11), habitacion INT, precio FLOAT,estado VARCHAR(50))")
# conexion_BBDD.commit()
# conexion_BBDD.close()


class Cliente():

    def __init__(self, Dni, Nombre, Edad, Telefono, Correo):
        self.Dni = Dni
        self.Nombre = Nombre
        self.Edad = Edad
        self.Telefono = Telefono
        self.Correo = Correo

    def __str__(self) -> str:
        return f'DNI: {self.Dni}, Nombre: {self.Nombre}'

    def eliminar_cliente(self):
        conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
        cursor = conexion_BBDD.cursor()
        sql_orden = f"DELETE FROM Clientes WHERE idCliente = {self.Dni}"
        cursor.execute(sql_orden)
        conexion_BBDD.commit()
        conexion_BBDD.close()

    def cliente_a_registro(self):
        # datos = (idCliente, Nombre, Edad, Telefono, Correo)
        conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
        cursor = conexion_BBDD.cursor()
        sql_orden = f"INSERT INTO Clientes (idCliente, Nombre, Edad, Telefono, Correo) VALUES ({self.Dni},'{self.Nombre}',{self.Edad},{self.Telefono},'{self.Correo}');"
        cursor.execute(sql_orden)
        conexion_BBDD.commit()
        conexion_BBDD.close()
        print(f"Se ha añadido el/la cliente {self.Nombre} a la base de datos")

    

class Reserva():

    def __init__(self, idReserva, Dni, Nombre, fecha_inicio, fecha_fin, habitacion, precio):
        self.idReserva = idReserva
        self.Dni = Dni
        self.Nombre = Nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.habitacion = habitacion
        self.precio = precio
        self.estado = "NO CONFIRMADA"

    def __str__(self) -> str:
        return f'Numero de reserva: {self.idReserva}, Nombre persona: {self.Nombre}'

    def reserva_a_registro(self):
        conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
        cursor = conexion_BBDD.cursor()
        sql_orden = f"INSERT INTO Reservas (idReserva, idCliente, Nombre, fecha_inicio, fecha_fin, habitacion, precio, estado) VALUES ({self.idReserva},{self.Dni},'{self.Nombre}','{self.fecha_inicio}','{self.fecha_fin}',{self.habitacion},{self.precio},'{self.estado}');"
        cursor.execute(sql_orden)
        conexion_BBDD.commit()
        conexion_BBDD.close()

    def eliminar_reserva(self):
        conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
        cursor = conexion_BBDD.cursor()
        sql_orden = f"DELETE FROM Reservas WHERE idReserva = {self.idReserva}"
        cursor.execute(sql_orden)
        conexion_BBDD.commit()
        conexion_BBDD.close()

    def confirmar_reserva(self):
        conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
        cursor = conexion_BBDD.cursor()
        sql_orden = f"UPDATE Reservas SET estado='CONFIRMADA' WHERE idReserva = {self.idReserva}"
        cursor.execute(sql_orden)
        conexion_BBDD.commit()
        conexion_BBDD.close()

        
def mostrar_cliente(Nombre):
    conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
    cursor = conexion_BBDD.cursor()
    sql_orden = f"SELECT * FROM Clientes WHERE Nombre = '{Nombre}';"
    cursor.execute(sql_orden)
    datos_cliente = cursor.fetchall()
    print(f"Datos del cliente:\n \tid:{datos_cliente[0][0]}\n \tNombre: {datos_cliente[0][1]}\n \tEdad: {datos_cliente[0][2]}\n \tTelefono: {datos_cliente[0][3]}\n \tCorreo: {datos_cliente[0][4]}\n")
    conexion_BBDD.close()

def mostrar_reserva(idReserva):
    conexion_BBDD = psycopg2.connect(database="Casa_Huespedes", user="postgres", password="Pepetijuelas28")
    cursor = conexion_BBDD.cursor()
    sql_orden = f"SELECT * FROM Reservas WHERE idReserva = '{idReserva}';"
    cursor.execute(sql_orden)
    datos_reserva = cursor.fetchall()
    print(f"Datos de reserva:\n \tid:{datos_reserva[0][0]}\n \tDNI cliente: {datos_reserva[0][1]}\n \tNombre: {datos_reserva[0][2]}\n \tFecha de inicio: {datos_reserva[0][3]}\n \tFecha final: {datos_reserva[0][4]}\n \tHabitacion: {datos_reserva[0][5]}\n \tPrecio: {datos_reserva[0][6]}\n \tEstado: {datos_reserva[0][7]}")
    sql_orden = f"SELECT * FROM Clientes WHERE Nombre = '{datos_reserva[0][2]}';"
    cursor.execute(sql_orden)
    datos_cliente = cursor.fetchall()
    print(f"Datos del cliente:\n \tid:{datos_cliente[0][0]}\n \tNombre: {datos_cliente[0][1]}\n \tEdad: {datos_cliente[0][2]}\n \tTelefono: {datos_cliente[0][3]}\n \tCorreo: {datos_cliente[0][4]}\n")
    conexion_BBDD.close()

Cliente_1 = Cliente(3,"Juan",29,659897356,"juanzamorarey@gmail.com")
# Cliente_1.cliente_a_registro()
# Cliente_1.eliminar_cliente()
Reserva_1 = Reserva(3,7654,"Juan","23/07/2022","28/07/2022",342,125.50)
# Reserva_1.reserva_a_registro()
mostrar_reserva(3)
Reserva_1.confirmar_reserva()
mostrar_reserva(3)