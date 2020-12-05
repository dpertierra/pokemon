from bs4 import BeautifulSoup
import requests
import shutil
import json
from models.attack import *
from constants import *

url = "https://pokemondb.net/pokedex/all"

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemon_dict = {}
pokemon_names = []

pokemon_rows = page_content.find_all("tr")
for row in pokemon_rows[1:650]:
    stats_html = row.find_all("td")[4:]
    stats_array = list(map(lambda poke_data: int(poke_data.text), stats_html))
    types_html = row.find_all("a", attrs={"class": "type-icon"})
    types_array = list(map(lambda poke_data: TYPES.index(poke_data.text), types_html))
    name_aux = name = row.find("a", attrs={"class": "ent-name"}).text
    name_aux = name_aux.lower().strip()
    # if '♂' in name_aux:
    name_aux = name_aux.replace("♂", "-m")
    # elif '♀' in name:
    name_aux = name_aux.replace("♀", "-f")
    # if "'" in name_aux:
    name_aux = name_aux.replace("'", "")
    name_aux = name_aux.replace(". ", '-')
    name_aux = name_aux.replace(" ", "-")
    pokemon_names.append(name_aux)
    mega_html = row.find("small", attrs={"class": "text-muted"})
    if not mega_html:
        pokemon_dict[name_aux] = {"type1":   types_array[0],
                                  HP:        stats_array[0],
                                  ATTACK:    stats_array[1],
                                  DEFENSE:   stats_array[2],
                                  SPATTACK:  stats_array[3],
                                  SPDEFENSE: stats_array[4],
                                  SPEED:     stats_array[5],
                                  "DisplayName": name}
        if len(types_array) > 1:
            pokemon_dict[name_aux]["type2"] = types_array[1]

# Saves pokemon data in a JSON file
with open('db/pokemons.json', 'w') as outfile:
    json.dump(pokemon_dict, outfile)

# Downloads pokemon images
for name in pokemon_names:
    front_image_url = f"https://img.pokemondb.net/sprites/black-white/normal/{name}.png"
    back_image_url = f"https://img.pokemondb.net/sprites/black-white/back-normal/{name}.png"
    resp_front = requests.get(front_image_url, stream=True)
    resp_back = requests.get(back_image_url, stream=True)
    with open(f"res/sprites/{name}_front.png", 'wb') as front_file:
        resp_front.raw.decode_content = True
        shutil.copyfileobj(resp_front.raw, front_file)
    with open(f"res/sprites/{name}_back.png", 'wb') as back_file:
        resp_back.raw.decode_content = True
        shutil.copyfileobj(resp_back.raw, back_file)


move_dict = {}
for i in range(1, 6):
    url_moves = "https://pokemondb.net/move/generation/" + str(i)
    page_response = requests.get(url_moves, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    move_rows = page_content.find_all("tr")
    for move in move_rows[1:]:
        move_name = move.find("a", attrs={"class": "ent-name"}).text
        move_html = move.find_all("td")[2:6]
        category = move_html[0].attrs["data-filter-val"]
        move_html = move_html[1:]
        move_array = list(map(lambda move_data: int(move_data.text) if move_data.text.isdigit() else 0, move_html))
        type_attack = move.find("a", attrs={"class": "type-icon"}).text
        if move_array[0] == 0:
            move_array[1] = 100
        move_dict[move_name] = {
            "type":     type_attack,
            "category": category,
            "power":    move_array[0],
            "accuracy": move_array[1],
            "pp":       move_array[2]
        }

with open('db/attacks.json', 'w') as outfile:
    json.dump(move_dict, outfile)

with open("db/pokemons.json", 'r') as file:
    data = json.load(file)

moves_by_pokemon = {}
for pkm_name in data.keys():
    url_moves_poke = "https://pokemondb.net/pokedex/" + pkm_name.lower() + "/moves/5"
    page_response = requests.get(url_moves_poke, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    move_table = page_content.find("table")
    moves_1_15 = moves_15_30 = moves_30_45 = moves_45_60 = moves_60_75 = moves_75_90 = []
    if move_table:
        move_rows_level = move_table.find_all("tr")
        for move in move_rows_level[1:]:
            name = move.find("a", attrs={"class": "ent-name"}).text
            move_html = move.find_all("td")
            move_level = int(move_html[0].text)
            category = move_html[3].attrs["data-filter-val"]
            type_attack = move.find("a", attrs={"class": "type-icon"}).text
            power = int(move_html[4].text) if move_html[4].text.isdigit() else 0
            accuracy = int(move_html[5].text) if move_html[5].text.isdigit() else 100

            attack = {"name": name,
                      "type": type_attack,
                      "category": category,
                      "pp": move_dict[name]["pp"],
                      "power": power,
                      "accuracy": accuracy}
            if 1 <= move_level <= 15:
                moves_1_15.append(attack)
            elif 15 < move_level <= 30:
                moves_15_30.append(attack)
            elif 30 < move_level <= 45:
                moves_30_45.append(attack)
            elif 45 < move_level <= 60:
                moves_45_60.append(attack)
            elif 60 < move_level <= 75:
                moves_60_75.append(attack)
            elif 75 < move_level <= 90:
                moves_75_90.append(attack)
            moves_by_pokemon[pkm_name] = {0: moves_1_15,
                                          1: moves_15_30,
                                          2: moves_30_45,
                                          3: moves_45_60,
                                          4: moves_60_75,
                                          5: moves_75_90
                                          }
    else:
        print(url_moves_poke)
print(moves_by_pokemon)
with open('db/moves_by_pokemon.json', 'w') as outfile:
    json.dump(moves_by_pokemon, outfile)
