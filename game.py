import pygame
from functools import partial
from pygame.locals import *
from constants import *
from models.attack import *
from models.battle import *
from models.pokemon import *
from models.button import *
from models.turn import *
from models.command import *
from models.menu import *
from models.GUI import *
import json
import math
from random import randint


def fillAttacks(pokemon):
    attacks = []
    with open("db/moves_by_pokemon.json", 'r') as moves_file:
        moves = json.load(moves_file)
        moves_poke = moves[pokemon.name]
        end_poke = math.ceil(pokemon.level / 15)

        if end_poke > 6:
            end_poke = 6
        start_poke = end_poke - 4 if end_poke > 3 else 0

        for i in range(start_poke, end_poke):
            attack_list = list(moves_poke[str(i)])
            rand_attack = randint(0, len(attack_list) - 1)
            a = attack_list[rand_attack]
            # for a in attack_list:

            attack = Attack(a["name"], TYPES.index(a["type"]), a["category"], a["pp"], a["power"], a["accuracy"])
            attacks.append(attack)
        if end_poke <= 3:
            for i in range(4 - end_poke):
                rand = randint(0, 4 - end_poke - 1)
                attack_list = list(moves_poke[str(rand)])
                rand_attack = randint(0, len(attack_list) - 1)
                a = attack_list[rand_attack]
                # for a in attack_list:
                attack = Attack(a["name"], TYPES.index(a["type"]), a["category"], a["pp"], a["power"], a["accuracy"])
                attacks.append(attack)
        return attacks


class Game:
    def __init__(self):
        self.buttons = []
        self.menu = Menu()
        self.gui = GUI()
        self.bg = None
        self.battle_finished = False
        self.again = False
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pokemon Battle!")

        clock = pygame.time.Clock()
        clock.tick(60)

        self.initPokemonStats()
        # Attacks
        # Button(500, 500, 100, 40, 'Attack', self.makeTurn)
        self.pokemon1.attacks = fillAttacks(self.pokemon1)
        self.pokemon2.attacks = fillAttacks(self.pokemon2)

        self.loadResources()
        print('Resources loaded successfully')
        # Start battle
        self.battle = Battle(self.pokemon1, self.pokemon2)

        self.stopped = False
        print('Initialization finished')

    def process(self):
        if self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0:
            # print("Test")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopped = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stopped = True
                for button in self.buttons:
                    button.handleEvent(event, self)
                self.menu.handleEvent(event, self)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        print(event.pos)

    def loadResources(self):
        self.loadPokemonImage(self.pokemon1, True)
        self.loadPokemonImage(self.pokemon2, False)
        self.gui.loadResources()

    def loadPokemonImage(self, pokemon, is_player):
        pokemon_name = pokemon.name.lower()
        if is_player:
            pokemon_img = pygame.image.load("res/sprites/" + pokemon_name + "_back.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (300, 300))
            pokemon.renderer = pokemon_img
        else:
            pokemon_img = pygame.image.load("res/sprites/" + pokemon_name + "_front.png")
            pokemon_img = pygame.transform.scale(pokemon_img, (200, 200))

            pokemon.renderer = pokemon_img
        self.bg = pygame.image.load("res/battle_bg/battle_bg_1.png")
        self.bg = pygame.transform.scale(self.bg, (800, 400))

    def initPokemonStats(self):
        # First define pokemons with its stats
        with open('db/pokemons.json') as f:
            data = json.load(f)
            rand_poke1 = randint(0, len(data.keys()) - 1)
            poke_names = list(data.keys())
            poke1_name = poke_names[rand_poke1]
            rand_poke2 = randint(0, len(data.keys()) - 1)
            level_poke2 = randint(1, 100)
            level_poke1 = randint(level_poke2 - 2, level_poke2 + 5)
            poke2_name = poke_names[rand_poke2]
            type2 = None
            if "type2" in data[poke1_name].keys():
                type2 = data[poke1_name]["type2"]
            self.pokemon1 = Pokemon(poke1_name, level_poke1, data[poke1_name]["type1"], type2,
                                    data[poke1_name]["DisplayName"])
            type22 = None
            if "type2" in data[poke2_name]:
                type22 = data[poke2_name]["type2"]
            self.pokemon2 = Pokemon(poke2_name, level_poke2, data[poke2_name]["type1"], type22,
                                    data[poke2_name]["DisplayName"])
            self.pokemon1.baseStats = {
                HP:        data[self.pokemon1.name]["HP"],
                ATTACK:    data[self.pokemon1.name]["Attack"],
                DEFENSE:   data[self.pokemon1.name]["Defense"],
                SPATTACK:  data[self.pokemon1.name]["SpAttack"],
                SPDEFENSE: data[self.pokemon1.name]["SpDefense"],
                SPEED:     data[self.pokemon1.name]["Speed"]
            }

            self.pokemon2.baseStats = {
                HP:        data[self.pokemon2.name]["HP"],
                ATTACK:    data[self.pokemon2.name]["Attack"],
                DEFENSE:   data[self.pokemon2.name]["Defense"],
                SPATTACK:  data[self.pokemon2.name]["SpAttack"],
                SPDEFENSE: data[self.pokemon2.name]["SpDefense"],
                SPEED:     data[self.pokemon2.name]["Speed"]
            }

        # self.pokemon1.ev = {
        #     HP:        randint(0,255),
        #     ATTACK:    0,
        #     DEFENSE:   0,
        #     SPATTACK:  0,
        #     SPDEFENSE: 0,
        #     SPEED:     0
        # }

        self.pokemon1.iv = {
            HP:        randint(0, 31),
            ATTACK:    randint(0, 31),
            DEFENSE:   randint(0, 31),
            SPATTACK:  randint(0, 31),
            SPDEFENSE: randint(0, 31),
            SPEED:     randint(0, 31)
        }

        # self.pokemon2.ev = {
        #     HP:        0,
        #     ATTACK:    0,
        #     DEFENSE:   0,
        #     SPATTACK:  0,
        #     SPDEFENSE: 0,
        #     SPEED:     0
        # }

        self.pokemon2.iv = {
            HP:        randint(0, 31),
            ATTACK:    randint(0, 31),
            DEFENSE:   randint(0, 31),
            SPATTACK:  randint(0, 31),
            SPDEFENSE: randint(0, 31),
            SPEED:     randint(0, 31)
        }
        self.pokemon1.computeStats()
        self.pokemon2.computeStats()
        print(self.pokemon1.stats)
        print(self.pokemon2.stats)
        self.pokemon1.current_hp = self.pokemon1.stats["HP"]
        self.pokemon2.current_hp = self.pokemon2.stats["HP"]
        print(self.pokemon1.current_hp, self.pokemon1.stats["HP"])

    def renderPokemons(self):
        pokemon_1size = self.pokemon1.renderer.get_rect().size
        self.pokemon1.render(self.screen, (10, 470 - pokemon_1size[1]))
        self.pokemon2.render(self.screen, (550, -20))

    def renderButtons(self):
        self.menu.render(self)
        self.gui.render(self)
        if self.pokemon1.current_hp > 0 and self.pokemon2.current_hp > 0:
            for button in self.buttons:
                button.render(self)

        if self.pokemon1.current_hp > 0 >= self.pokemon2.current_hp:
            self.gui.renderMessage(self, self.pokemon1.display_name + " has won!")
            self.battle_finished = True
        elif self.pokemon2.current_hp > 0 >= self.pokemon1.current_hp:
            self.gui.renderMessage(self, self.pokemon2.display_name + " has won!")
            self.battle_finished = True
        elif self.pokemon2.current_hp <= 0 and self.pokemon1.current_hp <= 0:
            self.gui.renderMessage(self, "Incredible! Double KO!")
            self.battle_finished = True
        else:
            self.gui.renderMessage(self, "What should " + self.pokemon1.display_name + " do?")

    def render(self):
        self.screen.fill((255, 255, 255))  # fill white
        if self.bg:
            self.screen.blit(self.bg, (0, 0))
        self.renderPokemons()
        self.renderButtons()
        pygame.display.update()

    def makeTurn(self, index):
        print('Using attack', index)
        turn = Turn()
        turn.command1 = Command({DO_ATTACK: index})
        turn.command2 = Command({DO_ATTACK: 0})

        if turn.canStart():
            # Execute turn
            if not self.battle.isFinished():
                self.battle.executeTurn(turn)
                self.battle.printCurrentStatus()
            else:
                self.battle.printWinner()

    def restart(self):
        # self.stopped = True
        self.again = True
