name = input("Please type your name: ")
last_name = input("And your last name is: ")
age = int(input("Please type your age: "))

if age < 3:
    result = "bebe"
elif age < 10:
    result = "niño"
elif age < 13:
    result = "preadolescente"
elif age < 18:
    result = "adolescente"
elif age < 25:
    result = "adulto joven"
elif age < 65:
    result = "Adulto"
else:
    result = "Adulto mayor"

print(f"Hola {name} {last_name}, según tu edad ({age} años), eres {result}.")