import random

# Constants
chance_caverna = 1
chance_mato = 1
chance_caprtura = 1

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
    captura = input(f"Deseja captura-lo? (sim/não) ")
    if captura.lower() == "sim":
        if capturar_pokemon(pokemon_encontrado, chance_caprtura):
            print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")
            pokemon_capturados.append(pokemon_encontrado)
        else:
            print(f"Infelizmente, o {pokemon_encontrado} fugiu!")

def encontrou_pokemon_caverna():
    if len(pokemon_capturados) < 3:
        return True
    else:
        resposta = input("Você já encontrou três Pokémons nesta caverna. Deseja fazer outra atividade? (sim/não) ").lower()
        if resposta == "sim":
            return True
        else:
            print("Continuando jornada...") 
            return False

def encontrou_pokemon_mato():
    if len(pokemon_capturados) < 3:
        return True
    else:
        resposta = input("Você já encontrou três Pokémons neste mato. Deseja fazer outra atividade? (sim/não) ").lower()
        if resposta == "sim":
            return True
        else:
            print("Continuando jornada...")
            return False

# Main loop
while True:
    menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()
    if menu == "explorar":
        ambiente = input("Em que ambiente deseja explorar? Digite 'caverna', 'mato': ").lower()
        if ambiente == "caverna":
            if encontrou_pokemon_caverna():
                pokemon_encontrado = pokemon_caverna()
                if pokemon_encontrado:
                    informar_pokemon_encontrado(pokemon_encontrado)
        elif ambiente == "mato":
            if encontrou_pokemon_mato():
                pokemon_encontrado = pokemon_mato()
                if pokemon_encontrado:
                    informar_pokemon_encontrado(pokemon_encontrado)
        else:
            print("Desculpe, não entendi. Por favor, digite 'caverna' ou 'mato'.")
            ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
            pokemon_encontrado = None if ambiente == "caverna" else pokemon_mato()

        if pokemon_encontrado:
            informar_pokemon_encontrado(pokemon_encontrado)
    elif menu == "pokedex":
        print("\nSeus Pokémons capturados são:")
        for pokemon in pokemon_capturados:
            print(f"- {pokemon}")
    elif menu == "sair":
        print("Até logo, aventureiro!")
        break
    else:
        print("Digite novamente")