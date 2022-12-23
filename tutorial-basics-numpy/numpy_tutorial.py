import numpy as np

# Numpy nos permite hacer varias cosas que una lista no permite:
# 1o - un numpy array es mucho más rápido que una lista porque cada número ocupa menos memoria
# 2o - un numpy array permite crear lista de n dimensiones ideal para vectores, matrices, etc.
# 


# ¿En qué son mejores las numpy arrays que las listas?

# si tuviermos por ejemplo
a = [1,2,3]
b = [4,5,6]

# No podemos ejecutar multiplicaciones de un elemento cada vez, es decir, 1*4, 2*5, 3*6...
# En cambio en numpy esto es posible:

a_np = np.array([1,2,3])
b_np = np.array([4,5,6])

c_np = a_np*b_np

# print(c_np)
# >>>[ 4 10 18]

# Saber numpy se torna fundamental para librerías como pandas, matplotlib, scipy... es fundamental para ML
# Para crear un array de numpy:

#  variable = np.array([[lista_valores],[lista_valores]...])

# Por cada lista de valores dentro de la lista general tendremos una dimensión
scalar_value_np = np.array([4.3])
# print(scalar_value_np)
# >>>[4.3]
vector_example_np = np.array([1.3,2.6,7.8])
# print(vector_example_np)
# >>> [1.3 2.6 7.8]
matrix_array_np = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matrix_array_np)
# >>>[[1 2 3]
#  >>>[4 5 6]
#  >>>[7 8 9]]
three_dimensions_tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# print(three_dimensions_tensor)
# >>>[[[ 1  2  3]
# >>>  [ 4  5  6]]

# >>> [[ 7  8  9]
# >>>  [10 11 12]]

# >>> [[13 14 15]
# >>> [16 17 18]]]

# Si quremos saber la dimension de un tensor guardado en un array de numpy

# variable.ndim

# print(three_dimensions_tensor.ndim)
# >>> 3

# Ver la forma de un array

# variable.shape


# print(matrix_array_np.shape)
# >>> (3, 3)


# --------------------------------------------------------------------------------SLICING, CHANGING, COLUMNS AND ROWS

X = np.array([[25,2],[5,26],[3,7]])

# En una matriz el slicing dependerá de sus dimensiones (mirar diagrama matriz)
# La matriz que usamos de ejemplo tiene esta forma, por tanto cuenta con 2 dimensiones como todas las matrices.
# También se pueden usar tensores de 3 dimensiones pero el slicing sería diferente, de momento centrémonos en el slicing
# de matrices:
# 25 2
# 5 26
# 3 7
# Si ponemos X[numero_fila, numero_columna] podemos rescatar scalars de la matriz. Por ejemplo el 26
# print(X[1,1])
# >>> 26
# También puedes usar los negativos para empezar a recorrer desde el final.
# print(X[1,-1])
# >>> 26
# Para rescatar secciones de la matriz seguimos la misma lógica. Si solo queremos la fila
# X[numero_fila], ejemplo la primera fila
# print(X[0])
# >>> [25  2]
# si por el contrario queremos la columna:
# X[:,numero_columna], ejemplo la primera columna
# print(X[:,0])
# >>> [25  5  3]
# Podemos también ser más exquisitos y pensar que solo queremos ciertas secciones de la matriz. Para ello usamos la siguiente sintaxis:
# [idnice_de_inicio:indice_final:tamaño_salto]
# Vamos a usar una matriz mas grande para ejemplificarlo
Y = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
# En el print seleccionamos pirmero la fila (0), después el elemento en el que quiero empezar (1) hasta el elemento en el que queremos
# terminar (6) [como queremos terminar en el 6 debemos incluir el 7 ya que es exclusivo] y por último el tamaño del salto
# que queremos mostrar (2), es decir, cada dos elementos nos mostrará uno, eso sería 2 3no 4 5no 6, es decir, 2,4,6
# print(Y[0,1:6:2])
# >>> [2 4 6]

# Link utilizado https://www.pythoninformer.com/python-libraries/numpy/index-and-slice/


# Imaginemos que queremos cambiar algo en nuestro array de numpy
# Solo tenemos que indicar el índice y hacer un igual. Vamos a cambiar el elemento 5 de la fila 1 por 20
Y[1,5] = 20

# print(Y)
# >>>[[ 1  2  3  4  5  6  7]
# >>> [ 8  9 10 11 12 20 14]]

# Estos cambios se pueden aplicar a filas o columnas enteras. Vamos a cambiar la 3a columna a todo 5 por ejemplo
Y[:,2] = 5
# print(Y)
# >>>[[ 1  2  5  4  5  6  7]
# >>> [ 8  9  5 11 12 20 14]]

# Podríamos especificar también un cambio más concreto, por ejemplo introduciendo la misma forma de lo que vamos a sutituir:
# Vamos a cambiar la columna 4 por 14 en la primera fila y 3 en la segunda.
Y[:,3] = [14, 3]

# print(Y)
# [[ 1  2  5 14  5  6  7]
#  [ 8  9  5  3 12 20 14]]

# Si trabajáramos con matrices de 3 dimensiones o mas debemos ir siempre desde fuera hacia dentro:
three_dimensions_tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])
# print(three_dimensions_tensor)
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 7  8  9]
#   [10 11 12]]

#  [[13 14 15]
#   [16 17 18]]]

# Imaginemos que queremos extraer el 11. De las 3 matrices queremos la 2a, de la segunda la 2a fila y de la fila el 2o elemento. 
# print(three_dimensions_tensor[1,1,1])
# >>> 11

# Para sutituir es lo mismo mientras se la misma dimension va a funcionar. Un truco es printear lo que interesa y después
# sustituir por algo que tenga el mismo formato. Imaginemos que queremos sustituir la segunda matriz por todo 1

# print(three_dimensions_tensor[1,:,:])
# [[ 7  8  9]
#  [10 11 12]]

three_dimensions_tensor[1,:,:] = [[1,1,1],[1,1,1]]
# print(three_dimensions_tensor)
# [[[ 1  2  3]
#   [ 4  5  6]]

#  [[ 1  1  1]
#   [ 1  1  1]]

#  [[13 14 15]
#   [16 17 18]]]


# ---------------------------------------------------------------------------------------INITIALIZING DIFFERENT TYPES OF ARRAYS

#  Generar una matriz de 0s de las dimensiones que queramos, por ejemplo 2 filas 3 columnas.

matriz_zeros = np.zeros((2,3))
# print(matriz_zeros)
# [[0. 0. 0.]
#  [0. 0. 0.]]

# Generar una matriz de todo 1s

matriz_unos = np.ones((2,3))
# print(matriz_unos)
# [[1. 1. 1.]
#  [1. 1. 1.]]

# Generar una matriz de cualquier otro valor. toma 2 parámetros, el 2o es el valor, el primero la forma. 
matriz_33 = np.full((2,3),33)
# print(matriz_33)
# [[33 33 33]
#  [33 33 33]]

# Generar una matriz con la misma forma que otra pero con diferentes valores. Por ejemplo matriz_33 con 99
matriz_99 = np.full_like(matriz_33,99)
# print(matriz_99)
# [[99 99 99]
#  [99 99 99]]

# Generar una matriz de numeros aleatorios entre 0 y 1
matriz_aleatoria = np.random.rand(2,3)
# print(matriz_aleatoria)
# [[0.41633748 0.97330794 0.8761642 ]
#  [0.99178417 0.28999274 0.46273139]]

# Si quieres pasarle una forma el metodo es random_sample
matriz_aleatoria = np.random.random_sample(matriz_99.shape)
# print(matriz_aleatoria)
# [[0.97355239 0.38695683 0.13117192]
#  [0.50381826 0.2623422  0.20432937]]


# Generar una matriz de numeros enteros aleatorios con la forma que queramos
# El primer número que pasemos será el máximo valor posible. Recordemos que es exlcuyente por lo que es el primer numero -1
# Si ponemos dos números se tomarán como un rango
matriz_aleatoria = np.random.randint(10,size=(3,3))
# print(matriz_aleatoria)
# [[5 7 0]
#  [5 5 0]
#  [3 0 9]]

matriz_aleatoria = np.random.randint(8,10,size=(3,3))
# print(matriz_aleatoria)
# [[9 9 8]
#  [8 9 8]
#  [8 9 9]]

# Generar una matriz de identidad del size deseado
matriz_identidad = np.identity(4)
# print(matriz_identidad)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Repetir una matriz varias veces
# axis = 0 indica el eje sobre el que se van a repetir las matrices. Se repetirá todo lo que esté dentro de la primera lista
matriz_repetida = np.array([[1,2,3]])
r_3 = np.repeat(matriz_repetida, 3, axis=0)
# print(r_3)
# [[1 2 3] 
#  [1 2 3] 
#  [1 2 3]]

matriz_repetida = np.array([1,2,3])
r_3 = np.repeat(matriz_repetida, 3)
# print(r_3)
# [1 1 1 2 2 2 3 3 3]



# Reconstruye esta matriz usando los conceptos aprendidos
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1
matriz_aleatoria = np.zeros((5,5))
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]
matriz_aleatoria[:,0] = 1
matriz_aleatoria[:,len(matriz_aleatoria)-1] = 1
matriz_aleatoria[0,:] = 1
matriz_aleatoria[len(matriz_aleatoria)-1,:] = 1
matriz_aleatoria[2,2] = 9
# print(matriz_aleatoria)
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]


# Cuidado al copiar arrays. Si no usamos la función copy() se alterará el valor en las dos variables que contengan el array
a = np.array([1,2,3])
b = a 
b[0] = 100
# print(a)
# >>>[100   2   3]

a = np.array([1,2,3])
b = a.copy() 
b[0] = 100
# print(a)
# print(b)
# >>> [1 2 3]
# >>> [100   2   3]




# --------------------------------------------------------------------- NUMPY MATHS

# Sumar a todos los elementos de una mtriz
a = np.array([1,2,3,4])
# print(a+2)
# # >>> [3 4 5 6]
# print(a-2)
# # [-1  0  1  2]
# print(a*2)
# # [2 4 6 8]
# print(a/2)
# [0.5 1.  1.5 2. ]

# aritmética entre dos listas
b = np.array([0,1,1,2])
# print(a+b)
# [1 3 4 6]

# Sacar el coseno del array
c = np.sin(b)
# print(c)
# [0.         0.84147098 0.84147098 0.90929743]

# -------------------------------------------------------------------------ALGEBRA LINEAL

# Mulitplicar funciones
a = np.ones((2,3))
b = np.full((3,2),2)

c = np.matmul(a,b)
# print(c)
# [[6. 6.]
#  [6. 6.]]


# Determinante de una matriz. En la matriz identidad debe dar 1
c = np.identity(3)
d = np.linalg.det(c)
# print(d)
# >>> 1.0

# Ver la inversa de una matriz
e = np.linalg.inv(c)
# print(e)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]


# --------------------------------------------------Statistics with numpy

stats = np.array([[1,2,3],[4,5,6]])
# print(stats)
# [[1 2 3]
#  [4 5 6]]
# Encontrar el minimoy el maimo
a = np.min(stats)
# print(a)
# 1
a = np.max(stats)
# print(a)
# 6

# También se puede hacer por filas. Cada fila será de la lista general. Devuelve el minimo de cada lista en el eje seleccionado
# axis indica el nivel de lista al que se realizan las operaciones
a = np.min(stats, axis=1)
# print(a)
# [1 4]
# Mira las dos listas
a = np.min(stats, axis=0)
# print(a)
# [1 2 3]
# Mira solo la lista 1

# Suma de valores en el array por dimensiones

a = np.sum(stats)
# print(a)
# 21

a = np.sum(stats, axis=0) # suma las filas entre sí
# print(a)
# [5 7 9]

a = np.sum(stats, axis=1) # suma las filas por separado
# print(a)
# [ 6 15]

# También se puede hacer a nivel de columna


# ---------------------------------------------------------------------REorganizar arrays

Y = np.array([[1,2,3,4],[5,6,7,8]])
# print(Y)
# [[1 2 3 4]
#  [5 6 7 8]]

# Unir una lista de acuerdo a un shpae determinado. debe ser compatible en dimensiones
Y_changed = Y.reshape((1,8))
# print(Y_changed)
# [[1 2 3 4 5 6 7 8]]

Y_changed = Y.reshape((8,1))
# print(Y_changed)
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]
#  [7]
#  [8]]

Y_changed = Y.reshape((4,2))
# print(Y_changed)
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]


# Unir matrices verticalmente. Puedes pasar un mismo vector varias vecess
X = np.array([[1,2,3,4]])
Y = np.array([[5,6,7,8]])

union_XY = np.vstack([X,Y])
# print(union_XY)
# [[1 2 3 4]
#  [5 6 7 8]]

union_XY = np.vstack([X,Y,X,Y])
# print(union_XY)
# [[1 2 3 4]
#  [5 6 7 8]
#  [1 2 3 4]
#  [5 6 7 8]]

# Unir matrices horizontalmente. Puedes pasar un mismo vector varias vecess
X = np.array([[1,2,3,4]])
Y = np.array([[5,6,7,8]])

union_XY = np.hstack([X,Y])
# print(union_XY)
# [[1 2 3 4 5 6 7 8]]

union_XY = np.hstack([X,Y,X,X,Y])
# print(union_XY)
# [[1 2 3 4 5 6 7 8 1 2 3 4 1 2 3 4 5 6 7 8]]


# ---------------------------------------------------------------------------------------Miscellanous things

# Open a txt file with dat and storage it in a numpy array. It directly cast data into float type

data = np.genfromtxt("file_numpy.txt",delimiter=",")
# print(data)
# [[1.00000000e+00 2.00000000e+00 3.00000000e+00 4.00000000e+00
#   5.00000000e+00 6.00000000e+00 7.00000000e+00 4.00000000e+00]
#  [1.34000000e+02 8.00000000e+00 5.43200000e+03 6.48900000e+03
#   2.34543223e+10 3.00000000e+00 4.00000000e+00 5.00000000e+00]
#  [3.40000000e-01 5.60000000e-01 5.60000000e-01 9.87000000e+00
#   4.56000000e+00 4.32000000e+00 5.67000000e+00 4.30000000e-01]]

# If you want to cast it to integer for example
# data = data.astype('int32')
# This changes data to int32 and change the . of floats for -
# print(data)
# [[          1           2           3           4           5           6         7           4]
#  [        134           8        5432        6489 -2147483648           3         4           5]
#  [          0           0           0           9           4           4         5          0]]
#             

# Importante: Si solo pones data.astype('int32') se crea una copia pero no se reasgina a la variable a menos que lo indiques


# Boolean masking and advance indexing

# Puedes realiar operadores lógicos booleanos sobre los datos y devuelve una matriz con valores superiores
# print(data > 10)
# [[False False False False False False False False]
#  [ True False  True  True  True False False False]
#  [False False False False False False False False]]

# También puedes indexar usando operadores lógicos
# print(data[data > 10])
# [1.34000000e+02 5.43200000e+03 6.48900000e+03 2.34543223e+10]

# Se puede indexar en un array de numpy
a = np.array([1,2,3,4,5,6,7,8])
b = a[[1,3,5,7]]
# print(b)
# [2 4 6 8]

# También podemos operar lógicamente a nivel de columnas. Por ejemplo cual de las columnas contiene valores superiores a 10.
# Situamos también el print de data para poder ver con más claridad el motivo de los true
c = np.any(data > 10, axis=0)
# print(data)
# print(c)
# [[          1           2           3           4           5           6         7           4]
#  [        134           8        5432        6489 -2147483648           3         4           5]
#  [          0           0           0           9           4           4         5          0]]
# [ True                 False        True        True        True        False     False      False]

# Podemos ver cual de las columnas tiene en todo su eje valores superiores a 10

d = np.all(data > 10, axis=0)
# print(d)
# [[          1           2           3           4           5           6         7           4]
#  [        134           8        5432        6489 -2147483648           3         4           5]
#  [          0           0           0           9           4           4         5          0]]
# [ True                 False        True        True        True        False     False      False]
# [False False False False False False False False]

# Es correcto. Ninguna de las columnas tiene en todos sus valores numeros superiores a 10

# Si cambiaramos axis a axis=1 se comrpobarían las filas en vez de las columnas

# Podemos introducir varios operadores al mismo tiempo usando una sintaxis muy similar a la de pendas. Recordemos que pandas está
# basado en nummpy
data = data.astype("int32")
# print(data)
# [[   1    2    3    4    5    6    7    4] 
#  [ 134    8 5432 6489 2332    3    4    5] 
#  [  34   56   56   87  456  432  567   43]]
#   

# Numeros mayores que 10 y menores que 100 en la matriz
# print((data > 10) & (data < 100))
# [[False False False False False False False False]
#  [False False False False False False False False]
#  [ True  True  True  True False False False  True]]

# La matriz tiene algún número mayor que 10 y menor que 100
# print(np.any((data > 10) & (data < 100)))
# True
# print(np.all((data > 10) & (data < 100)))
# False


# Para hacer una negación usamos la sintaxis ~(expresion). Veremos que es el contrario de la expresion anterior
# print(~((data > 10) & (data < 100)))
# [[ True  True  True  True  True  True  True  True]
#  [ True  True  True  True  True  True  True  True]
#  [False False False False  True  True  True False]]


# Ejercicio. Tenemos esta matriz:
X = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
# print(X)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]
#  [26 27 28 29 30]]

# 1. queremos recuperar solo 11, 12, 16 y 17. 
# Importante el elemento final es siempre exclusivo por lo que hay que poner +1. Por ejemplo para coger elementos de la linea 4 se pone
# 4 pero si queremos empezar en la linea 4 se pone 3

X_indexada = X[2:4,0:2]
# print(X_indexada)
# [[11 12]
#  [16 17]]

# 2. queremos recuperar la diagonal que hacen 2, 8, 14 y 20. Seleccionas primero las filas y luego las columnas a seleccionar para
# esas filas

# print(X[[0,1,2,3],[1,2,3,4]])
# [ 2  8 14 20]

# 3. Queremos recuperar 4, 5, 24, 25, 29 y 30

print(X[[0,4,5],3:])
# [[ 4  5]
#  [24 25]
#  [29 30]]