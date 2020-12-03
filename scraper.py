from bs4 import BeautifulSoup
import requests
import shutil
import json
from constants import *

url = "https://pokemondb.net/pokedex/all"

page_response = requests.get(url, timeout=5)

page_content = BeautifulSoup(page_response.content, "html.parser")

pokemon_data = []
pokemon_dict = {}
pokemon_names = []

pokemon_rows = page_content.find_all("tr")
for row in pokemon_rows[1:]:
    stats_html = row.find_all("td")[4:]
    stats_map = map(lambda data: int(data.text), stats_html)
    stats_array = list(stats_map)
    types_html = row.find_all("a", attrs={"class": "type-icon"})
    types_map = map(lambda data: TYPES.index(data.text), types_html)
    types_array = list(types_map)
    name = row.find("a", attrs={"class": "ent-name"}).text
    pokemon_names.append(name.lower())
    mega_html = row.find("small", attrs={"class": "text-muted"})
    if mega_html:
        name = mega_html.text
    pokemon_dict[name] = {"type1": types_array[0],
                          HP: stats_array[0],
                          ATTACK: stats_array[1],
                          DEFENSE: stats_array[2],
                          SPATTACK: stats_array[3],
                          SPDEFENSE: stats_array[4],
                          SPEED: stats_array[5]}
    if len(types_array) > 1:
        pokemon_dict[name]["type2"] = types_array[1]

# Saves pokemon data in a JSON file
with open('db/pokemons.json', 'r') as outfile:
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
