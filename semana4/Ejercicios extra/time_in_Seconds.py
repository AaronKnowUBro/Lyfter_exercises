seconds = int(input("Por favor ingrese el timpo en segundos: "))

if seconds < 600:
    less = 600 - seconds
    print(f"faltan {less} para llegar a 10 minutos")
elif seconds > 600:
    print("Mayor")
else:
    print("Igual")