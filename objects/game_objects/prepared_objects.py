import json
import os

from objects.game_objects.ship.ship_layer_model import ShipLayer
from objects.game_objects.ship.ship_tile import ShipTile


def load_materials():
    with open('data/materials.json') as json_file:
        return json.load(json_file)


def load_tile_types():
    with open('data/tile_types.json') as json_file:
        return json.load(json_file)


def load_ships():
    with open('data/notations.json') as json_file:
        notations = json.load(json_file)
    result = {}
    i = 0
    for file in os.listdir('data/prepared_objects/ships'):
        with open('data/prepared_objects/ships/' + file) as ship_file:
            lines = ship_file.readlines()
            current_layer = []
            for line in lines[2:]:
                ship_line = []
                if bool(line.isspace()) or line == 'end':
                    layer = ShipLayer(current_layer)
                    result[i] = layer
                    current_layer = []
                    i = + 1
                    continue

                data = line.split()
                j = 0
                for obj in data:
                    if len(obj) == 2:
                        if obj != '..':
                            # get material
                            material = materials_map.get(notations.get('materials').get(obj[0]))
                            # get tile type
                            tile_type = tile_types_map.get(notations.get('tile_types').get(obj[1]))
                            ship_line.append(ShipTile(j, i, tile_type=tile_type, material=material))
                        else:
                            ship_line.append(ShipTile(j, i))
                    j = + 1
                current_layer.append(ship_line)
    return result


materials_map = load_materials()
tile_types_map = load_tile_types()
ships_map = load_ships()
