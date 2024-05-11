import random

chance_caverna = 0.5
chance_mato = 0.5
chance_captura = 0.5
chance_pokebolas = 0.3

pokemons_iniciais = ["Charmander", "Squirtle", "Bulbasaur"]
pokemons_caverna = ["Zubat", "Grimer", "Cubone", "Geodude"]
pokemons_mato = ["Pidgey", "Rattata", "Ekans", "Oddish"]

nome_jogador = input("Qual é o seu nome aventureiro? ")
print(f"Olá {nome_jogador}, prepare-se para uma emocionante jornada!")

pokebolas = 3

pokemon_capturados = []

primeiro_pokemon = []

def pokemon_inicial(primeiro_pokemon):
    pokemon_inicial = input("Escolha um dos seguintes pokemons para começar a sua jornada: Charmander, Squirtle, Bulbasaur\n").lower()
    while pokemon_inicial not in ["charmander", "squirtle", "bulbasaur"]:
        print("Desculpe, não entendi. Por favor, digite um pokemon válido.")
        pokemon_inicial = input("Escolha um dos seguintes pokemons para começar a sua jornada: Charmander, Squirtle, Bulbasaur\n").lower()
    primeiro_pokemon.append(pokemon_inicial)
    pokemon_capturados.append(pokemon_inicial)
    return print(f"Seu pokemon inicial foi confirmado como: -{primeiro_pokemon[0]}-")

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
    global pokebolas
    print(f"\nParabéns, {nome_jogador}! Você encontrou um {pokemon_encontrado}!")
    captura = input(f"Deseja captura-lo? (sim/não) ").lower()
    while captura not in ["sim", "não"]:
        print("Desculpe, não entendi. Por favor, digite 'sim' ou 'não'.")
        captura = input(f"Deseja captura-lo? (sim/não) ").lower()

    if captura == "sim":
        if pokemon_encontrado in pokemon_capturados:
            print("Você já possui este Pokemon")
        else:
            pokebolas -= 1
            print(80*"-")
            print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")
            print(80*"-")
            pokemon_capturados.append(pokemon_encontrado)
    elif captura == "não":
        print("Ok, voltando para o menu...")
    else:
        print(f"Infelizmente, o {pokemon_encontrado} fugiu!")

def adquirir_pokebolas():
    global pokebolas
    print(f"Você possui:{pokebolas}, pokebolas")
    if random.random() < chance_pokebolas:
        qtd_pokebolas = random.randint(1, 2)
        pokebolas += qtd_pokebolas
        print(f"Parabéns, {nome_jogador}! Você adquiriu {qtd_pokebolas} pokebolas!")
    else:
        print("Nenhuma pokebola adquirida desta vez")


def menu():
    global pokebolas
    pokemon_inicial(primeiro_pokemon)
    while True:
        menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()
        while menu not in ["explorar", "pokedex", "sair"]:
            print("Desculpe, não entendi. Por favor, digite 'explorar', 'pokedex' ou 'sair'.")
            menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()

        if menu == "explorar":
            if pokebolas > 0:
                ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
                if ambiente == "caverna":
                    pokemon_encontrado = pokemon_caverna()
                    if pokemon_encontrado:
                        adquirir_pokebolas()
                        informar_pokemon_encontrado(pokemon_encontrado)
                        if pokemon_encontrado not in pokemon_capturados:
                         print(f"Nenhuma pokebola gasta")
                         print(80*"-")
                        else:
                         print(f"Você gastou 1 pokebola.")
                         print(80*"-")
                        pokebolas -= 1
                elif ambiente == "mato":
                    pokemon_encontrado = pokemon_mato()
                    if pokemon_encontrado:
                        adquirir_pokebolas()
                        informar_pokemon_encontrado(pokemon_encontrado)
                        if pokemon_encontrado not in pokemon_capturados:
                         print(f"Nenhuma pokebola gasta")
                         print(80*"-")
                        else:
                         print(f"Você gastou 1 pokebola.")
                         print(80*"-")
                        pokebolas -= 1
                else:
                    print("Desculpe, não entendi. Por favor, digite 'caverna' ou 'mato'.")
            else:
                print("Você não tem mais pokebolas. Não é mais possivel Explorar")
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