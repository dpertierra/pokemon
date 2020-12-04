import pygame
from pygame.locals import *
from functools import partial
from constants import *
from models.battle import *
from models.pokemon import *
from models.attack import *
from models.button import *
from models.menu import *
from models.GUI import *
import json

class Game:
    def __init__(self, pkm1, pkm2):
        self.buttons = []
        self.menu = Menu()
        self.gui = GUI()
        self.bg = None
        pygame.init()

        self.screen = pygame.display.set_mode((160*4, 144*4))
        pygame.display.set_caption("Pokemon Battle")
        clock = pygame.time.Clock()
        clock.tick(60)

        self.initPokemonStats()
        #Attacks
        #Button(500, 500, 100, 40,'Attack', self.makeTurn)
        self.pokemon1.attacks = [
            Attack("Headbutt", 0, PHYSICAL, 10, 80, 100)
            Attack("Headbutt", 0, PHYSICAL, 10, 80, 100)
        ]