import random

from constants import *


class Battle:
    def __init__(self, pokemon1, pokemon2):
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.actual_turn = 0

    def isFinished(self):
        finished = self.pokemon1.current_hp <= 0 or self.pokemon2.current_hp <= 0
        if finished:
            self.printWinner()
        return finished

    def executeTurn(self, turn):
        command1 = turn.command1
        command2 = turn.command2
        attack1 = None
        attack2 = None
        if DO_ATTACK in command1.action.keys() and self.pokemon1.current_hp > 0:
            attack1 = self.pokemon1.attacks[command1.action[DO_ATTACK]]
        if DO_ATTACK in command2.action.keys() and self.pokemon2.current_hp > 0:
            attack2 = self.pokemon2.attacks[command2.action[DO_ATTACK]]

        self.pokemon2.current_hp -= self.computeDamage(attack1, self.pokemon1, self.pokemon2)
        self.pokemon1.current_hp -= self.computeDamage(attack2, self.pokemon2, self.pokemon1)

        self.actual_turn += 1

    def computeDamage(self, attack, pokemon1, pokemon2) -> float:
        aux = ((2 * pokemon1.level) / 5) + 2
        power_factor = aux * attack.power
        if attack.category == PHYSICAL:
            power_factor *= (pokemon1.stats[ATTACK] / pokemon2.stats[DEFENSE])
        else:
            power_factor *= (pokemon1.stats[SPATTACK] / pokemon2.stats[SPDEFENSE])
        damage_without_modifier = power_factor / 50 + 2

        return damage_without_modifier * self.computeDamageModifier(attack, pokemon1, pokemon2)

    def computeDamageModifier(self, attack, pokemon1, pokemon2) -> float:
        stab = 1
        if attack.type == pokemon1.type1 or attack.type == pokemon1.type2:
            stab = 1.5
        effective1 = TYPE_CHART[attack.type][pokemon2.type]
        effective2 = TYPE_CHART[attack.type][pokemon2.type2]
        effective_final = effective1 * effective2
        critical = 1
        if random.random() < 0.1:
            critical = 1.5
        return stab * effective_final * critical

    def printWinner(self):
        if self.pokemon1.current_hp <= 0 < self.pokemon2.current_hp:
            print(f"{self.pokemon1.name} won in {self.actual_turn}")
        elif self.pokemon2.current_hp <= 0 < self.pokemon1.current_hp:
            print(f"{self.pokemon2.name} won in {self.actual_turn}")
        else:
            print("Double KO")

    def printCurrentStatus(self):
        if self.pokemon1.current_hp > 0:
            print(f"{self.pokemon1.name} has {self.pokemon1.current_hp} HP left")
        if self.pokemon2.current_hp > 0:
            print(f"{self.pokemon2.name} has {self.pokemon2.current_hp} HP left")
