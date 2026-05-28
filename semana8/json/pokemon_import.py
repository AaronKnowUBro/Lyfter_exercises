import json

JSON_FILE = "pokemon.json"

def load_pokemons():
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("El archivo no existe, se creará uno nuevo.")
        return []
    except json.JSONDecodeError:
        print("El archivo JSON está dañado o vacío. Se iniciará una lista nueva.")
        return []

def get_new_pokemon():
    name = input("Ingrese el nombre del Pokémon: ")
    type_ = input("Ingrese el tipo del Pokémon: ")

    while True:
        try:
            level = int(input("Ingrese el nivel del Pokémon: "))
            if level <= 0:
                print("El nivel debe ser un número mayor a 0.")
                continue
            break
        except ValueError:
            print("Error: el nivel debe ser un número válido.")

    return {
        "name": name,
        "type": type_,
        "level": level
    }

def save_pokemons(pokemons):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(pokemons, file, indent=4, ensure_ascii=False)

def show_pokemons(pokemons):
    print("Contenido actual del archivo JSON:")
    print(json.dumps(pokemons, indent=4, ensure_ascii=False))

def main():
    pokemons = load_pokemons()
    new_pokemon = get_new_pokemon()
    pokemons.append(new_pokemon)
    save_pokemons(pokemons)
    print("Pokémon agregado correctamente.\n")
    show_pokemons(pokemons)

main()