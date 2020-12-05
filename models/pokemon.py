from constants import *


class Pokemon:
    def __init__(self, name, level, type1, type2, display_name):
        self.name = name
        self.level = level
        self.type = type1
        self.type2 = type2
        self.attacks = []  # Attack Array
        self.stats = {}
        self.baseStats = {}
        # self.ev = {}
        self.iv = {}
        self.current_status = 0
        self.current_hp = 0
        self.nature = 0
        self.renderer = None
        self.display_name = display_name

    def render(self, screen, position):
        if self.renderer:
            screen.blit(self.renderer, position)

    def computeStats(self):
        self.stats = {
            HP:        self.computeHPStat(),
            ATTACK:    self.computeStandardStat(ATTACK),
            DEFENSE:   self.computeStandardStat(DEFENSE),
            SPATTACK:  self.computeStandardStat(SPATTACK),
            SPDEFENSE: self.computeStandardStat(SPDEFENSE),
            SPEED:     self.computeStandardStat(SPEED)
        }

    def computeStandardStat(self, stat):
        value = (2 * self.baseStats[stat] + self.iv[stat]) * self.level  # + self.ev[stat] // 4) * self.level
        return (value // 100 + 5) * NATURE_MATRIX[self.nature][stat]

    def computeHPStat(self):
        value = (2 * self.baseStats[HP] + self.iv[HP]) * self.level  # + self.ev[HP] // 4) * self.level
        return value // 100 + self.level + 10
