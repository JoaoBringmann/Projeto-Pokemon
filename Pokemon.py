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
    
def informar_pokemon_encontrado(pokemon_encontrado):
    print(f"\nParabéns, {nome_jogador}! Você encontrou um {pokemon_encontrado}!")
    captura = input((f"Deseja captura-lo? (sim/não)"))
    if captura == "sim":
        if random.random() < chance_captura:
            capturar_pokemon(pokemon_encontrado)
            print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")
        else:
            print(f"Infelizmente, o {pokemon_encontrado} fugiu!")

def capturar_pokemon(pokemon_encontrado):
    global pokemon_capturados

    if pokemon_encontrado in pokemon_capturados:
        print(f"O {pokemon_encontrado} já está na sua Pokédex, {nome_jogador}!")
    else:
        pokemon_capturados.append(pokemon_encontrado)
        print(f"Parabéns, {nome_jogador}! Você capturou um {pokemon_encontrado}!")

def encontrou_pokemon():
    if len(pokemon_capturados) < 3:
        return True
    else:
        resposta = input("Você já encontrou três Pokémons neste ambiente. Deseja procurar em outro ambiente? (sim/não) ").lower()
        if resposta == "sim":
            ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
            if ambiente == "caverna":
                pokemon_encontrado = pokemon_caverna()
            elif ambiente == "mato":
                pokemon_encontrado = pokemon_mato()
            else:
                print("Digite Novamente uma das Opções.")
                ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
                pokemon_encontrado = None if ambiente == "caverna" else pokemon_mato()
            return encontrou_pokemon()
        else:
            print("Tudo bem, volte quando quiser tentar novamente!")
            return False

while True:
    menu = input("O que deseja fazer?\nExplorar\nPokedex\nSair\n").lower()
    if menu == "explorar":
        ambiente = input("Em que ambiente deseja explorar? Digite 'caverna' ou 'mato': ").lower()
        if ambiente == "caverna":
            pokemon_encontrado = pokemon_caverna()
        elif ambiente == "mato":
            pokemon_encontrado = pokemon_mato()
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