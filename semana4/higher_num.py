first_num = int(input("Please type the first number: "))
second_num = int(input("Please type the second number: "))
third_num = int(input("Please type the third number: "))

higher_num = first_num

if second_num > higher_num:
    higher_num = second_num

if third_num > higher_num:
    higher_num = third_num

print(f"El número mayor ingresado es: {higher_num}")