from bs4 import BeautifulSoup
import requests
import shutil
import json
from constants import *

# url = "https://pokemondb.net/pokedex/all"
#
# page_response = requests.get(url, timeout=5)
#
# page_content = BeautifulSoup(page_response.content, "html.parser")
#
# pokemon_dict = {}
# pokemon_names = []
#
# pokemon_rows = page_content.find_all("tr")
# for row in pokemon_rows[1:]:
#     stats_html = row.find_all("td")[4:]
#     stats_array = list(map(lambda data: int(data.text), stats_html))
#     types_html = row.find_all("a", attrs={"class": "type-icon"})
#     types_array = list(map(lambda data: TYPES.index(data.text), types_html))
#     name = row.find("a", attrs={"class": "ent-name"}).text
#     pokemon_names.append(name.lower())
#     mega_html = row.find("small", attrs={"class": "text-muted"})
#     if mega_html:
#         name = mega_html.text
#     pokemon_dict[name] = {"type1":   types_array[0],
#                           HP:        stats_array[0],
#                           ATTACK:    stats_array[1],
#                           DEFENSE:   stats_array[2],
#                           SPATTACK:  stats_array[3],
#                           SPDEFENSE: stats_array[4],
#                           SPEED:     stats_array[5]}
#     if len(types_array) > 1:
#         pokemon_dict[name]["type2"] = types_array[1]
#
# # Saves pokemon data in a JSON file
# with open('db/pokemons.json', 'r') as outfile:
#     json.dump(pokemon_dict, outfile)
#
# # Downloads pokemon images
# for name in pokemon_names:
#     front_image_url = f"https://img.pokemondb.net/sprites/black-white/normal/{name}.png"
#     back_image_url = f"https://img.pokemondb.net/sprites/black-white/back-normal/{name}.png"
#     resp_front = requests.get(front_image_url, stream=True)
#     resp_back = requests.get(back_image_url, stream=True)
#     with open(f"res/sprites/{name}_front.png", 'wb') as front_file:
#         resp_front.raw.decode_content = True
#         shutil.copyfileobj(resp_front.raw, front_file)
#     with open(f"res/sprites/{name}_back.png", 'wb') as back_file:
#         resp_back.raw.decode_content = True
#         shutil.copyfileobj(resp_back.raw, back_file)
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
        move_array = list(map(lambda data: int(data.text) if data.text.isdigit() else 0, move_html))
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
print(move_dict["Absorb"])

