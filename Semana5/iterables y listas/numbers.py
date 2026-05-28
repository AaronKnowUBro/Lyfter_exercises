numbers = []

for counter in range(10):
    list_num = int(input(f"Ingrese el número {counter + 1}: "))
    numbers.append(list_num)

print("Los números que ingresó son:", numbers)

mayor = numbers[0]
for num in numbers:
    if num > mayor:
        mayor = num

print("El número más alto fue:", mayor)


