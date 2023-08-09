tipo_impositivo = int(input("¿cuales son tus beneficios anuales?: "))

if tipo_impositivo < 10000:
    print("Te corresponde un tipo impositivo del 5%")
elif tipo_impositivo > 10000 and tipo_impositivo <= 20000:
        print("Te corresponde un tipo impositivo del 15%")
elif tipo_impositivo > 20000 and tipo_impositivo <= 35000:
        print("Te corresponde un tipo impositivo del 20%")
elif tipo_impositivo > 350000 and tipo_impositivo <= 60000:
        print("Te corresponde un tipo impositivo del 30%")
else:
    print("Te corresponde un tipo impositivo del 45%")






# Renta 	Tipo impositivo
# Menos de 10000€ 	5%
# Entre 10000€ y 20000€ 	15%
# Entre 200000€ y 35000€ 	20%
# Entre 350000€ y 60000€ 	30%
# Más de 60000€ 	45%