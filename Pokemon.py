import random

# Constants
chance_caverna = 0.5
chance_mato = 0.5
chance_captura = 0.5

# Lists
pokemons_caverna = ["Zubat", "Grimer", "Cubone", "Geodude"]
pokemons_mato = ["Pidgey", "Rattata", "Ekans", "Oddish"]

# Player's name
nome_jogador = input("Qual é o seu nome aventureiro? ")
print(f"Olá {nome_jogador}, prepare-se para uma emocionante jornada!")

# Initialize empty list for captured pokemons
pokemon_capturados = []

# Functions
def sorteio_pokemon(lista_pokemon):
    return random.choice(lista_pokemon)

def capturar_pokemon(pokemon, prob):
    return random.random() < prob

def pokemon_caverna():
    if random.random() < chance_caverna:
        return sorteio_pokemon(pokemons_caverna)
    else:
        print("Nenhum Pokémon apareceu nesta exploração.")
        return None

def pokemon_mato():
    if random.random() < chance_mato:
        return sorteio_pokemon(pokemons_mato)
    else:
        print("Nenhum Pokémon apareceu nesta exploração.")
        return None

def informar_pokemon_encontrado(pokemon_encontrado):
    print(f"\nParabéns, {nome_jogador}! Você encontrou um {pokemon_encontrado}!")
    captura = input(f"Deseja captura-lo? (sim/não) ").lower()
    while captura not in ["sim", "não"]:
        print("Desculpe, não entendi. Por favor, digite 'sim' ou 'não'.")
        captura = input(f"Deseja captura-lo? (sim/não) ").lower()

    if captura == "sim":
        if pokemon_encontrado in pokemon_capturados:
            print("Você já possui este Pokemon")
        else:
            print(80*"-")
            print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")
            print(80*"-")
            pokemon_capturados.append(pokemon_encontrado)
    elif captura == "não":
        if capturar_pokemon(pokemon_encontrado, chance_captura):
            print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")
            pokemon_capturados.append(pokemon_encontrado)
        else:
            print(f"Infelizmente, o {pokemon_encontrado} fugiu!")
        
def menu():
    while True:
        menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()
        while menu not in ["explorar", "pokedex", "sair"]:
            print("Desculpe, não entendi. Por favor, digite 'explorar', 'pokedex' ou 'sair'.")
            menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()

        if menu == "explorar":
            ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
            if ambiente == "caverna":
                pokemon_encontrado = pokemon_caverna()
                if pokemon_encontrado:
                    informar_pokemon_encontrado(pokemon_encontrado)
            elif ambiente == "mato":
                pokemon_encontrado = pokemon_mato()
                if pokemon_encontrado:
                    informar_pokemon_encontrado(pokemon_encontrado)
            else:
                print("Desculpe, não entendi. Por favor, digite 'caverna' ou 'mato'.")
        elif menu == "pokedex":
            print("\nSeus Pokémons capturados são:")
            for pokemon in pokemon_capturados:
             print(80*"-")
             print(f"- {pokemon}")
             print(80*"-")
        elif menu == "sair":
            print("\nObrigado por explorar este mundo Pokémon! Até a próxima!\n")
            break

menu()