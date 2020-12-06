import pygame
from functools import partial
from models.button import *


class Menu:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.rect = pygame.Rect(0, 400, 800, 600)
        self.state = 0
        self.main_buttons = [
            Button(460, 410, 150, 40, "Attack", partial(self.changeMenuState, new_state=1)),
            Button(460, 470, 150, 40, "Pokemon", partial(self.changeMenuState, new_state=2)),
            Button(625, 410, 150, 40, "Bag", partial(self.changeMenuState, new_state=3)),
            Button(625, 470, 150, 40, "Run", partial(self.changeMenuState, new_state=4))
        ]
        self.attack_buttons = []

    def handleEvent(self, event, game):
        for button in self.main_buttons:
            button.handleEvent(event)
        if self.state == 1:
            # Build and store attack buttons if first time
            if len(self.attack_buttons) == 0:
                attack_list = list(game.pokemon1.attacks)
                self.attack_buttons.append(Button(225, 410, 200, 40, attack_list[0].name,
                                                  partial(game.makeTurn, index=0)))
                self.attack_buttons.append(Button(5, 470, 200, 40, attack_list[1].name,
                                                  partial(game.makeTurn, index=1)))
                self.attack_buttons.append(Button(225, 470, 200, 40, attack_list[2].name,
                                                  partial(game.makeTurn, index=2)))
                self.attack_buttons.append(Button(5, 410, 200, 40, attack_list[3].name,
                                                  partial(game.makeTurn, index=3)))
            for button in self.attack_buttons:
                button.handleEvent(event)

    def changeMenuState(self, new_state):
        if self.state == 1 and new_state != 1:
            # ANY button clicked when LUCHAR MODE is ON, go BACK
            self.state = 0
            for button in self.main_buttons:
                button.enable()
        else:
            self.state = new_state
            for button in self.main_buttons:
                button.disable()

    def render(self, game):
        # pygame.draw.rect(game.screen, (0,0,0), self.rect, 4)
        for button in self.main_buttons:
            button.render(game)
        if self.state == 1:
            # Draw attack buttons
            for button in self.attack_buttons:
                button.render(game)
