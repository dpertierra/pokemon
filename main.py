from constants import *
from models.battle import *
from models.command import *
from models.pokemon import *
from models.turn import *

pokemon1 = Pokemon("Charmander", 100, 1, None)
pokemon2 = Pokemon("Bulbasaur", 100, 2, 10)

battle = Battle(pokemon1, pokemon2)


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


while not battle.isFinished():
    command1 = askCommand(pokemon1)
    command2 = askCommand(pokemon2)
    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.canStart():
        battle.executeTurn(turn)
        battle.printCurrentStatus()

