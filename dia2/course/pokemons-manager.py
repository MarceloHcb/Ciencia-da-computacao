import json

with open("pokemons.json") as pokemon_file:
    pokemons = json.load(pokemon_file)

for pokemon in pokemons['results']:
    print(pokemon['name'])
# print(pokemons[0] )
# print(pokemons['results']["name"])
# print(type(pokemons))
