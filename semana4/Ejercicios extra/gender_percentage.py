woman = 0
men = 0

for counter in range(0,6):
    gender = int(input("Por favor indique con el numero 1 si es mujer, o con el numero 2 si es hombre: "))
    if gender == 1:
        woman = woman + 1
    elif gender == 2:
        men = men + 1

woman_percentage = (woman / 6) * 100
men_percentage = (men / 6) * 100

print(f"El porcentaje de mujeres es de: {woman_percentage:.2f}%")
print(f"El porcentaje de hombres es de: {men_percentage:.2f}%")
