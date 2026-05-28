import random

secret_num = random.randint(1, 10)
user_num = None

print("Serás capaz de adivinar el numero secreto del 1 al 10?")

while user_num != secret_num:
    user_num = int(input("Ingresa tu numero: "))

    if user_num < secret_num:
        print("Casi, pero el numero secreto es mayor a ese, por favor intenta de nuevo")
    elif user_num > secret_num:
        print("Uy!, el numero secreto es menor a ese, por favor intenta de nuevo")
    else:
         print("Increible, eres como akinator, adivinaste el numero")
