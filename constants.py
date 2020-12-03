HP = "HP"
ATTACK = "Attack"
DEFENSE = "Defense"
SPATTACK = "SpAttack"
SPDEFENSE = "SpDefense"
SPEED = "Speed"

PHYSICAL = "physical"
SPECIAL = "special"


DO_ATTACK = "attack"
DO_ATTACK_SELECTION = "selected attack"


NATURE_MATRIX = [
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Hardy
    {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Lonely
    {HP: 1, ATTACK: 1.1, DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 0.9}, #Brave
    {HP: 1, ATTACK: 1.1, DEFENSE: 1,   SPATTACK: 0.9, SPDEFENSE: 1,   SPEED: 1},   #Adamant
    {HP: 1, ATTACK: 1.1, DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 0.9, SPEED: 1},   #Naughty
    {HP: 1, ATTACK: 0.9, DEFENSE: 1.1, SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Bold
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Docile
    {HP: 1, ATTACK: 1,   DEFENSE: 1.1, SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 0.9}, #Relaxed
    {HP: 1, ATTACK:1,    DEFENSE: 1.1, SPATTACK: 0.9, SPDEFENSE: 1,   SPEED: 1},   #Impish
    {HP: 1, ATTACK: 1,   DEFENSE: 0.9, SPATTACK: 1,   SPDEFENSE: 1.1, SPEED: 1},   #Lax
    {HP: 1, ATTACK: 0.9, DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1.1}, #Timid
    {HP: 1, ATTACK: 1,   DEFENSE: 0.9, SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1.1}, #Hasty
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Serious
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 0.9, SPDEFENSE: 1,   SPEED: 1.1}, #Jolly
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 0.9, SPEED: 1.1}, #Naive
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1.1, SPDEFENSE: 1,   SPEED: 0.9}, #Modest
    {HP: 1, ATTACK: 1,   DEFENSE: 0.9, SPATTACK: 1.1, SPDEFENSE: 1,   SPEED: 1},   #Mild
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1.1, SPDEFENSE: 1,   SPEED: 0.9}, #Quiet
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Bashful
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1.1, SPDEFENSE: 0.9, SPEED: 1},   #Rash
    {HP: 1, ATTACK: 0.9, DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1.1, SPEED: 1},   #Calm
    {HP: 1, ATTACK: 1,   DEFENSE: 0.9, SPATTACK: 1,   SPDEFENSE: 1.1, SPEED: 1},   #Gentle
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1.1, SPEED: 0.9}, #Sassy
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 0.9, SPDEFENSE: 1.1, SPEED: 1},   #Careful
    {HP: 1, ATTACK: 1,   DEFENSE: 1,   SPATTACK: 1,   SPDEFENSE: 1,   SPEED: 1},   #Quirky
]

NATURES = [
"Hardy",
"Lonely",
"Brave",
"Adamant",
"Naughty",
"Bold",
"Docile",
"Relaxed",
"Impish",
"Lax",
"Timid",
"Hasty",
"Serious",
"Jolly",
"Naive",
"Modest",
"Mild",
"Quiet",
"Bashful",
"Rash",
"Calm",
"Gentle",
"Sassy",
"Careful",
"Quirky"
]

TYPES =[
    "Normal",
    "Fighting",
    "Flying",
    "Poison",
    "Ground",
    "Rock",
    "Bug",
    "Ghost",
    "Steel",
    "Fire",
    "Water",
    "Grass",
    "Electric",
    "Psychic",
    "Ice"
    "Dragon",
    "Dark",
    "Fairy"
]

TYPE_CHART = [
    [1,	1,	1,	1,	1,	0.5, 1,	0, 0.5,	1,	1,	1,	1,	1,	1,	1,	1,	1,], #Normal Attacking
    [2,	1, 0.5, 0.5, 1,	2, 0.5, 0, 2, 1, 1, 1,	1,	0.5, 2,	1, 2, 0.5], #Fighting Attacking
    [1,	2, 1, 1, 1, 0.5, 2,	1, 0.5, 1, 1, 2, 0.5, 1, 1,	1, 1, 1], #Flying Attacking
    [1, 1, 1, 0.5, 0.5, 0.5, 1, 0.5, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2], #Poison Attacking
    [1, 1, 0, 2, 1, 2, 0.5, 1, 2, 2, 1, 0.5, 2, 1, 1, 1, 1, 1], #Ground Attacking
    [1, 0.5, 2, 1, 0.5, 1, 2, 1, 0.5, 2, 1, 1, 1, 1, 2, 1, 1, 1], #Rock Attacking
    [1, 0.5, 0.5, 0.5, 1, 1, 1, 0.5, 0.5, 0.5, 1, 2, 1, 2, 1, 1, 2, 0.5], #Bug Attacking
    [0, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 0.5, 1], #Ghost Attacking
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],

]
