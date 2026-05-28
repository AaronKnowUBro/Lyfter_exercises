import csv

def write_csv(file_path, data, headers):
    with open(file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for fila in reader:
            print(fila)

headers = ('nombre', 'genero', 'desarrollador', 'clasificacion')

videojuegos = []

while True:
    try:
        n = int(input("¿Cuántos videojuegos desea ingresar? "))
        if n <= 0:
            print("Por favor ingrese un número mayor a 0.")
            continue
        break
    except ValueError:
        print("Error: debe ingresar un número válido.")

for counter in range(n):
    print(f"\nVideojuego #{counter + 1}")

    nombre = input("Nombre: ")
    genero = input("Género: ")
    desarrollador = input("Desarrollador: ")
    clasificacion = input("Clasificación ESRB: ")

    juego = {
        'nombre': nombre,
        'genero': genero,
        'desarrollador': desarrollador,
        'clasificacion': clasificacion
    }

    videojuegos.append(juego)

write_csv('videojuegos.csv', videojuegos, headers)

print("\nArchivo 'videojuegos.csv' creado exitosamente.\n")
print("Contenido del archivo:")

read_csv('videojuegos.csv')
