# La pizzería Bella Napoli ofrece pizzas vegetarianas
#  y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

#     Ingredientes vegetarianos: Pimiento y tofu.
#     Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

# Escribir un programa que pregunte al usuario si quiere 
# una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
#  Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
#   Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

pizza = int(input("¿Quieres una pizza:  1.vegetariana o 2.no vegetariana? "))

if pizza == 1:
    ingrediente = int(input("Los ingredientes son: \n 1. pimiento \n 2. tofu \n ¿Cuál quieres?"))
    if ingrediente == 1:
        print("Tu pizza es vegetariana y lleva tomate, mozzarella y pimiento")
    elif ingrediente == 2:
        print("Tu pizza es vegetariana y lleva tomate, mozzarella y tofu")
elif pizza == 2:
    ingrediente = int(input("Los ingredientes son: \n 1. Peperoni \n 2. Jamón \n 3.Salmón \n ¿Cuál quieres?"))
    if ingrediente == 1:
        print("Tu pizza es no vegetariana y lleva tomate, mozzarella y Peperoni")
    elif ingrediente == 2:
        print("Tu pizza es no vegetariana y lleva tomate, mozzarella y Jamón")
    elif ingrediente == 3:
        print("Tu pizza es no vegetariana y lleva tomate, mozzarella y Salmón")
else:
    print("Tienes que elegir una pizza vegetariana (1) o no vegetariana (2)")

