import json

from constants import *
from models.battle import *
from models.command import *
from models.pokemon import *
from models.turn import *
import pygame
from pygame.locals import *

with open("db/pokemons.json", 'r') as file:
    data = json.load(file)


def fillBaseStats(pokemon, stats):
    if "type2" in stats:
        pokemon.type2 = stats["type2"]
    pokemon.baseStats = {HP:        stats["HP"],
                         ATTACK:    stats["Attack"],
                         DEFENSE:   stats["Defense"],
                         SPATTACK:  stats["SpAttack"],
                         SPDEFENSE: stats["SpDefense"],
                         SPEED:     stats["Speed"]
                         }
    return pokemon

pokemon_name = "Charmander"
pokemon1 = Pokemon(pokemon_name, 100, data[pokemon_name]["type1"], None)
pokemon1 = fillBaseStats(pokemon1, data[pokemon1.name])

pokemon_name = "Bulbasaur"
pokemon2 = Pokemon(pokemon_name, 100, data[pokemon_name]["type1"], None)
pokemon2 = fillBaseStats(pokemon2, data[pokemon2.name])

battle = Battle(pokemon1, pokemon2)


def render(screen):
    screen.fill((255, 255, 255))
    renderPokemons(screen, pokemon1, pokemon2)
    pygame.display.update()


def update():
    pass


def loadResources():
    loadPokemonImage(pokemon1, True)
    loadPokemonImage(pokemon2, False)


def loadPokemonImage(pokemon, is_player):
    pkm_name = pokemon.name.lower()
    pkm_name = pkm_name.strip()
    pkm_name = pkm_name.replace(' ', '')
    if is_player:
        image = f"res/sprites/{pkm_name}_back.png"
        print(image)
        pokemon_img = pygame.image.load(image)
    else:
        image = f"res/sprites/{pkm_name}_front.png"
        print(image)
        pokemon_img = pygame.image.load(image)
    pokemon_img = pygame.transform.scale(pokemon_img, (400, 400))
    pokemon.renderer = pokemon_img


def renderPokemons(screen, pokemon1, pokemon2):
    pokemon1.render(screen, (0, 300))
    pokemon2.render(screen, (400, -80))


def askCommand(pokemon):
    command = None
    while not (tmp_command := input(f"What should {pokemon.name} do?").split(" ")):
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Pokemon Battle")
    loadResources()
    clock = pygame.time.Clock()
    stopped = False
    clock.tick(60)
    while not game.stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stopped = True
        '''
        command1 = askCommand(pokemon1)
        command2 = askCommand(pokemon2)
        turn = Turn()
        turn.command1 = command1
        turn.command2 = command2
    
        if turn.canStart():
            battle.executeTurn(turn)
            battle.printCurrentStatus()
        '''
        update()
        render(screen)


if __name__ == "__main__":
    main()
