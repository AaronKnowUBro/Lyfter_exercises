class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Hace un sonido"

class Dog(Animal):
    def speak(self):
        return "Guau"

class Cat(Animal):
    def speak(self):
        return "Miau"

while True:
    animal_type = input("Ingrese el tipo de animal que quieres crear (perro/gato): ").lower()

    try:
        if animal_type == "perro":
            name_input = input("Ingrese el nombre del perrito: ")
            animal = Dog(name_input)
        elif animal_type == "gato":
            name_input = input("Ingrese el nombre del gato: ")
            animal = Cat(name_input)
        else:
            raise ValueError("Tipo de animal no válido. Por favor, ingrese 'perro' o 'gato'.")

        print(f"{animal.name} dice: {animal.speak()}")
        break

    except ValueError as e:
        print("Error:", e)
        print("Inténtalo de nuevo...\n")
