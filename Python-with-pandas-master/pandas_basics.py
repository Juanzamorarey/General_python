from msilib.schema import AdminExecuteSequence
import pandas as pd


# Pandas nos sirve para analizar datos y analizarlos de forma inemdiata y eficiente.
# Se integra perfectamente con archivos de tipo csv, xls, parquet, html, hdf5, json, gbq, SQL...
# Esto hace que resulte perfecta para cualquier tipo de análisis. 
# Además Pandas se conecta muy bien con librerias de representación de datos tales como matplotlib

#Pandas trabaja con Dataframes, es decir, marcos de datos que se colocan en forma de filas y columnas
#Cada dataframe tiene por tanto ffilas y columnas, cada columna tiene su tipo de dato (no podemos tener datos string y int
# en la misma columna). Cada columna y fila se identifica por un nombre y un índice (el índice no se sulee utilizar)
# 

#Empecemos a trabajar por tanto con pandas.

#-------------------------------------------- FUNCION .read_csv() --> lee archivos del tipo csv
df = pd.read_csv("excel_pruebas.csv", index_col="id")

#Ahora tenemos un dataframe con los datos de nuestro excel de pruebas
print(df)

#       Empleado          Puesto  Edad      Sueldo
# 0         Pepe        contable    43        1500
# 1          Ana  Administradora    32        1800
# 2         Juan        Conserje    21        1000
# 3    Valentine     tocapelotas    19         200
# 4  Marsupilami     putomaquina    23  1000000000

# Como podemos ver Pandas nos imprime un dataframe (DF). Este DF posee unos id para las columnas llamado header y 
# a su vez un índice que crea automáticamente para cada fila. Este índice se puede borrar posteriormente. Normalmente 
# Lo que hacemos es establecer una columna con el valor id de modo que los elementos de nuestros datos sean identificados
#a partir de dicho id, con pandas podremos entonces elegir qué columa funcionará como id de nuestros elementos:
#-------------------------------------------- FUNCION .read_csv(path, index_col = "valor_columna_id") --> lee archivos del tipo csv

# id      Empleado          Puesto  Edad      Sueldo
# 0         Pepe        contable    43        1500
# 1          Ana  Administradora    32        1800
# 2         Juan        Conserje    21        1000
# 3    Valentine     tocapelotas    19         200
# 4  Marsupilami     putomaquina    23  1000000000

# Lo primero que debemos hacer al usar pandas es ver cómo están nuestros datos. Para esto podemos usar estas funciones
# para visualizar.
# .head() muestra solo las primeras 5 filas de nuestros datos o tail() que muestra las ultimas 5 filas. a estas funciones
#se les puede introducir un numero como argumento de modo que muestren ese numero de filas

print(df.head(3))

# id    Empleado  Puesto  Edad  Sueldo
# 0      Pepe        contable    43    1500
# 1       Ana  Administradora    32    1800
# 2      Juan        Conserje    21    1000

print(df.tail(3))

# id    Empleado       Puesto  Edad      Sueldo
# 2          Juan     Conserje    21        1000
# 3     Valentine  tocapelotas    19         200
# 4   Marsupilami  putomaquina    23  1000000000

# También se pueden ver describir los datos usando estadísticos descriptivos. Para ello nos valemos de la funcion describe()
# que devuelve otro DF con la información que deseamos.

print(df.describe())

#             Edad        Sueldo
# count   5.000000  5.000000e+00
# mean   27.600000  2.000009e+08
# std     9.939819  4.472131e+08
# min    19.000000  2.000000e+02
# 25%    21.000000  1.000000e+03
# 50%    23.000000  1.500000e+03
# 75%    32.000000  1.800000e+03
# max    43.000000  1.000000e+09

# Este nuevo DF nos muestra datos como el conteo, la media, la mediana, el valor minimo, los percentiles... 

# El siguiente paso sería limpiar nuestros datos. Esto puede ser eliminar o llenar celdas con valores por defecto.
# para esto pandas nos ofrece la funcion dropna() para mostrarla vamos a añadir un dato vacío a nuestro csv y 
# mostrar el antes y el después.

print(df)


# id      Empleado          Puesto  Edad      Sueldo
# 0          Pepe        contable    43        1500
# 1           Ana  Administradora    32        1800
# 2          Juan        Conserje    21        1000
# 3     Valentine     tocapelotas    19         200
# 4   Marsupilami     putomaquina    23  1000000000
# 5       Antonio             NaN    34         430

df_filtrado = df.dropna()
print(df_filtrado)


# id      Empleado          Puesto  Edad      Sueldo
# 0          Pepe        contable    43        1500
# 1           Ana  Administradora    32        1800
# 2          Juan        Conserje    21        1000
# 3     Valentine     tocapelotas    19         200
# 4   Marsupilami     putomaquina    23  1000000000

# COmo podemos ver en el primer DF aparecía como numero 5 Antonio con un campo vacío y el valor NaN y en el segundo este
# elemento ha sido eliminado.

# Si no quisiera eliminar estos datos podría usar .fillna(0) que rellenará con 0 y no se borrará la línea

df_filtrado = df.fillna(0)
print(df_filtrado)

# id      Empleado          Puesto  Edad      Sueldo
# 0          Pepe        contable    43        1500
# 1           Ana  Administradora    32        1800
# 2          Juan        Conserje    21        1000
# 3     Valentine     tocapelotas    19         200
# 4   Marsupilami     putomaquina    23  1000000000
# 5       Antonio               0    34         430

# Podemos ver que el campo vacío de ANtonio aparece relleno con el valor que hemos asignado
# También podríamos rellenar datos dependiendo de la columna pasando como argumento un diccionario:

df_filtrado = df.fillna({"Puesto":"contable_2"})
print(df_filtrado)

# id      Empleado          Puesto  Edad      Sueldo
# 0          Pepe        contable    43        1500
# 1           Ana  Administradora    32        1800
# 2          Juan        Conserje    21        1000
# 3     Valentine     tocapelotas    19         200
# 4   Marsupilami     putomaquina    23  1000000000
# 5       Antonio      contable_2    34         430


#  Si solamente quisiéramos analizar solo una parte de los datos podemos hacer lo que se llaman filtrados. 
# Por ejemplo si solo queremos usar una columna

columna_empleado = df["Empleado"]
print(columna_empleado)

# id
# 0           Pepe
# 1            Ana
# 2           Juan
# 3      Valentine
# 4    Marsupilami
# 5        Antonio

# Si quisiera traer varias columnas tendría que definir una lista con el nombre de las columnas que quiero:
columna_empleado_sueldo = df[["Empleado","Sueldo"]]
print(columna_empleado_sueldo)

# id      Empleado      Sueldo
# 0          Pepe        1500
# 1           Ana        1800
# 2          Juan        1000
# 3     Valentine         200
# 4   Marsupilami  1000000000
# 5       Antonio         430

# Ahí tenemos un DF nuevo. 
# Pero ¿y si quisiéramos traer solo una o un rango de filas?. Para ello podemos usar un identificador o a través del índice
# de dichas filas.

# Filtrado a través de índices con iloc[] que tomar como argumento un índice numérico. si ponemos un numero
# : y otro numero obtendremos un rango por filas hasta uno antes del numero que indiquemos

print(df.iloc[2]) #fila 2
print(df.iloc[2:4]) #filas 2 y 3

# 2        Juan     Conserje    21    1000
# 3   Valentine  tocapelotas    19     200

# Para idnentificar individualemtne las filas y no por rangos debemos pasar una lista con los ídnices deseados:

print(df.iloc[[0,2,4]])

# id      Empleado       Puesto  Edad  Sueldo
# 0          Pepe     contable    43        1500
# 2          Juan     Conserje    21        1000
# 4   Marsupilami  putomaquina    23  1000000000

# Si quisiéramos filtrar por identificadores solamente debemos cambiar la función quitándole la i

print(df.loc[2]) #fila 2
print(df.loc[2:4]) #filas 2 y 3

# Podemos filtrar también simultáneameente filas y columnas. Para ello con la misma función .loc() podemos hacerlo pasándole
# una doble lista. en la primera con las filas y en la segunda con el nombre de las columnas

print(df.loc[[2,4], ["Empleado"]])


# id      Empleado
# 2          Juan
# 4   Marsupilami

# Podríamos pasar varias columnas a la segunda lsita ya también se filtrarían. 
# El filtrado mas interesante llega cuando introducimos condiciones. para ello tenemos la siguiente sintaxis:

print(df[df["Sueldo"] > 1200])
# Del DF coge la columna sueldo y devuelveme aquellos elementos cuyo valor en dicha columna sea sueprior a 1200

# id      Empleado          Puesto  Edad      Sueldo
# 0          Pepe        contable    43        1500
# 1           Ana  Administradora    32        1800
# 4   Marsupilami     putomaquina    23  1000000000

# Para concatenar condiciones tenemos que recordar varias cosas. Cada condición se debe encerrar entre () y
# para establecer condiciones unidas utilizamos &. Siendo así:

print(df[(df["Sueldo"] > 1200) & (df["Edad"] < 30)])
# Del df coge aquellos cuyo sueldo sea mas de 1200 y tengan una edad menos a 30 años

# id      Empleado          Puesto  Edad      Sueldo
# 4   Marsupilami     putomaquina    23  1000000000

# Estos filtros de búsqueda se pueden aplicar tambiémn con datos tipo string viendo que strings contienen otros strg

# print(df[df["Puesto"].str.contains("contable")]) #da error
# Da error porque hay un NaN en nuestro dataframe para esta columna, usemos el DF ya filtrado
print(df_filtrado[df_filtrado["Puesto"].str.contains("contable")]) #da error

# 0      Pepe    contable    43    1500
# 5   Antonio  contable_2    34     430


# Previa a la aplicación de algoritmos muchas veces existe una fase de transformación de datos. Esto es:
# A partir de los datos ya existentes, se crean nuevas columnas que tengan datos transofrmados. Imaginemos que 
# queremos introducir una nueva fila en la que conste el dinero total que ha ganado cada empleado, suponiendo
# que la empresa lleva en pie 4 años y todos los empleados estuvieron desde el principio con sus sueldos actuales. 

# Primero definimos la función de transfomración del dato:

def dinero_por_anno(sueldo):
    dinero_total = sueldo * 4
    return dinero_total

# Una vez definida la función procedemos a añadir la columna. para ello decimos df["nueva_fila"] = df["fila_afectada"].apply("funcion")
ahorro = df["Ahorro"] = df["Sueldo"].apply(dinero_por_anno)

print(ahorro.head())

# id      Empleado          Puesto  Edad      Sueldo     Ahorro
# 0          Pepe        contable    43        1500        6000
# 1           Ana  Administradora    32        1800        7200
# 2          Juan        Conserje    21        1000        4000
# 3     Valentine     tocapelotas    19         200         800
# 4   Marsupilami     putomaquina    23  1000000000  4000000000

# Ahí tenemos nuestra nuevo columna. Veamos ahora si quisiéramos llevar a cabo aún más complejas operaciones
# usando varias columnas de la fila.

# Imaginemos entonces que  queremos obtener la edad que tenían los empleados cuando empezaron a trabajar, a partir 
# de su ahorro y su edad en la tabla. Para ello dividiremos el Ahorro entre el sueldo y el resultado lo restaremos
# a la edad

def edad_inicial(fila):
    annos_en_empresa = fila["Ahorro"] / fila["Sueldo"]
    annos_al_inicio = fila["Edad"] - annos_en_empresa
    return (annos_al_inicio)

annos_empresa = df["Lleva_en_la_empresa"] = df.apply(edad_inicial, axis=1)
# Axis indica a apply que la función debe aplicarse a cada fila del dataframe
print(annos_empresa.head())

      
# id      Empleado          Puesto  Edad      Sueldo      Ahorro  Lleva_en_la_empresa
# 0          Pepe        contable    43        1500        6000                 39.0
# 1           Ana  Administradora    32        1800        7200                 28.0
# 2          Juan        Conserje    21        1000        4000                 17.0
# 3     Valentine     tocapelotas    19         200         800                 15.0
# 4   Marsupilami     putomaquina    23  1000000000  4000000000                 19.0

# Como vemos aquí nos aparece la edad que tenía cada persona 

# Cuando ya tengo todos mis datos tal y como los quiero viene la fase de agrupación. En otras palabras: unir filas que 
# tengan el mismo valor en una columna determinada. Para ello vamos a añadir algunas personas más a nuestra empresa. 
# Supongamos que queremos agrupar los datos a partir de la columna Puesto, de modo que, haya una sola fila para los
# puestos que son iguales la cual estará agrupada de acuerdo al promedio

print(df.groupby("Puesto").mean())

#                 Edad        Sueldo        Ahorro  Lleva_en_la_empresa
# Puesto
# Administradora  32.0  1.800000e+03  7.200000e+03                 28.0
# Conserje        22.0  9.500000e+02  3.800000e+03                 18.0
# contable        49.5  1.750000e+03  7.000000e+03                 45.5
# putomaquina     23.0  1.000000e+09  4.000000e+09                 19.0
# tocapelotas     19.0  2.000000e+02  8.000000e+02                 15.0

# En este DF vemos por tanto para todas las filas el promedio respecto a las otras columnas a partir de una. Es decir,
# la media de sueldo para cada puesto agrupando a todas las personas que tienen el mismo puesto, la media de edad, etc.
# IMPORTANTE: en este DF recién creado ahora los datos más a la izquierda han pasado a ser os id. 

# Esta función es editable hasta el punto de que podemos pasar un diccioario de python eligiendo qué agrupación queremos
#para cada columna

agrupacion = df.groupby("Puesto").agg({
    "Sueldo":"mean",
    "Edad":"max",
    "Ahorro":"sum"
})

print(agrupacion)

# Aquí pedimos agrupar (.agg) por puesto y en la columna sueldo nos aparecerá la media para cada puesto,
#  en la de edad la más alta para cada puesto y
# en la de ahorro la suma total de lo que la empresa ha gastado en los trabajadores con ese puesto en los últimos 4 meses

#                    Sueldo  Edad      Ahorro
# Puesto
# Administradora        1800    32        7200
# Conserje               950    23        7600
# contable              1750    56       14000
# putomaquina     1000000000    23  4000000000
# tocapelotas            200    19         800

# Luego podemos realizar operaciones sobre los DF ya creados. Para la visualización de datos podemos usar la librería
# matplotlib, primero vamos a importarla:

import matplotlib.pyplot as plt 

# Si quisiéramos graficar el DF que acabamos de hacer lo haríamos de esta manera:

# df["Sueldo"].plot()

# plt.show()

# Esto mostrará un gráfico de líneas que, es posible que no se vea como nosotros deseamos. Siendo así si quisiéramos
# cambiarlo a un gráfico de barras solamente deberíamos hacer esto:

# agrupacion["Sueldo"].plot(kind = "bar")

# plt.show()

# La graficación puede usarse a su vez con solamente dos variables las cuales queramos relacionar por algún motivo. 
# Para ello vamos a volver a nuestro DF original y establecer la relación entre puesto y Sueldo por ejemplo. El kind
# scatter implica establecer un valor para el eje de las x y otro valor para el eje de ls y

try:
    df.plot(kind="scatter", x="Puesto", y="Sueldo")

    plt.show()
except:
    print("Error en el gráfico")

# Por último imaginemos que queremos guardar nuestro DF, para ello es tan sencillo como usar el metodo .to_csv()

agrupacion.to_csv("salida.csv")