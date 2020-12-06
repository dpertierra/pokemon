import pygame
from functools import partial
from models.button import *
from pygame.locals import *
import os


class GUI:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(os.path.join("res", "font", "font.ttf"), 15)
        self.rect = pygame.Rect(0, 800, 800, 600)
        self.rendererPlayer = None
        self.rendererEnemy = None

    def loadResources(self):
        player_gui = pygame.image.load('res/gui/life_bar_player.png')
        size = player_gui.get_rect().size
        aspect_ratio = int(size[0] / size[1])
        player_gui = pygame.transform.scale(player_gui, (100 * aspect_ratio, 100))
        self.rendererPlayer = player_gui

        enemy_gui = pygame.image.load('res/gui/life_bar_enemy.png')
        size = enemy_gui.get_rect().size
        aspect_ratio = int(size[0] / size[1])
        enemy_gui = pygame.transform.scale(enemy_gui, (75 * aspect_ratio, 75))
        self.rendererEnemy = enemy_gui

    def renderHPBar(self, game, bar_size, total_hp, actual_hp, position):
        percentage = float(actual_hp) / total_hp
        color = "green"
        if percentage < 0.5:
            color = "orange"
        if percentage < 0.15:
            color = "red"
        bar = pygame.Rect(position, (bar_size * percentage, 20))
        game.screen.fill(Color(color), bar)

    def renderMessage(self, game, text):
        text_surface = self.font.render(text, False, (0, 0, 0))
        game.screen.blit(text_surface, (50, 550))

    def render(self, game):
        total_player_hp = game.pokemon1.stats["HP"]
        total_enemy_hp = game.pokemon2.stats["HP"]
        self.renderHPBar(game, 186, total_enemy_hp, game.pokemon2.current_hp, (112, 60))
        self.renderHPBar(game, 180, total_player_hp, game.pokemon1.current_hp, (572, 304))

        if self.rendererEnemy:
            text_surface = self.font.render(game.pokemon2.display_name, False, (0, 0, 0))
            game.screen.blit(text_surface, (20, 30))

            text_surface = self.font.render("Lv:" + str(game.pokemon2.level), False, (0, 0, 0))
            game.screen.blit(text_surface, (250, 30))

            text_surface = self.font.render(str(int(game.pokemon2.current_hp)) + "/" + str(int(total_enemy_hp)), False,
                                            (0, 0, 0))
            game.screen.blit(text_surface, (110, 90))

            game.screen.blit(self.rendererEnemy, (20, 50))
        if self.rendererPlayer:
            text_surface = self.font.render(game.pokemon1.display_name, False, (0, 0, 0))
            game.screen.blit(text_surface, (510, 278))

            text_surface = self.font.render("Lv:" + str(game.pokemon1.level), False, (0, 0, 0))
            game.screen.blit(text_surface, (690, 278))

            text_surface = self.font.render(str(int(game.pokemon1.current_hp)) + "/" + str(int(total_player_hp)), False,
                                            (0, 0, 0))
            game.screen.blit(text_surface, (570, 330))

            game.screen.blit(self.rendererPlayer, (480, 298))

        self.renderMessage(game, "")
