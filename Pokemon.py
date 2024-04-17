import random

pokemon_capturados = []

nome_jogador = input("Qual é o seu nome aventureiro? ")
print(f"Olá {nome_jogador}, prepare-se para uma emocionante jornada!")

chance_caverna = 0.5
chance_mato = 0.5
chance_captura = 0.5
pokemons_caverna = ["Zubat", "Grimer", "Cubone", "Geodude"]
pokemons_mato = ["Pidgey", "Rattata", "Ekans", "Oddish"]

def pokemon_caverna():
    if random.random() < chance_caverna:
        return random.choice(pokemons_caverna)
    else:
        print("Nenhum Pokémon apareceu nesta exploração.")
        return None

def pokemon_mato():
    if random.random() < chance_mato:
        return random.choice(pokemons_mato)
    else:
        print("Nenhum Pokémon apareceu nesta exploração.")
        return None