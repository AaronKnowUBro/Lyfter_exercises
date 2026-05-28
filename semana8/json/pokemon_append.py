import json

file = "pokemon.json"

try:
    with open(file, "r", encoding="utf-8") as f:
        pokemones = json.load(f)
except FileNotFoundError:
    pokemones = []

name = input("Nombre del Pokémon: ")
pokemon_type = input("Tipo del Pokémon: ")
level = int(input("Nivel del Pokémon: "))

new_pokemon = {
    "nombre": name,
    "tipo": pokemon_type,
    "nivel": level
}

pokemones.append(new_pokemon)

with open(file, "w", encoding="utf-8") as f:
    json.dump(pokemones, f, indent=2, ensure_ascii=False)

print("El Pokémon fue agregado correctamente.")

print("\nLista actual de Pokémon:")
for p in pokemones:
    print(p)
