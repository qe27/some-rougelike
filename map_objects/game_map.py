from map_objects import random_map_generator
from map_objects.map_types import *
from map_objects.tile_objects.tile import Tile
from objects.game_objects.world_map.settlement import Settlement


class Map:

    def __init__(self, width, height, map_type=WORLD_MAP):
        self.width = width
        self.height = height
        self.map_type = map_type
        self.map_offset = (0, 0)
        self.selected_tile = (0, 0)
        self.tiles = self.initialize_tiles()
        self.make_map()

    def initialize_tiles(self):
        tiles = [[Tile(self, x, y) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self):
        if self.map_type == WORLD_MAP:
            generated_map = random_map_generator.generate_random_map_values()
            print(generated_map)
            for x in range(self.width):
                for y in range(self.height):
                    if generated_map.n[x + 1][y + 1] > 0.3:
                        self.tiles[x][y].tile_object = Settlement()
        if self.map_type == LOCATION_MAP:
            for x in range(self.width):
                for y in range(self.height):
                    if x % 2 and y % 3:
                        self.tiles[x][y].tile_object = Settlement()
            # if self.parent_type=
            # else:
            #     self.tiles[x][y].tile_object.set_landscape({River(): 1})
            # if (x == 10) or (y == 15):
            #     self.tiles[x][y].tile_structure.set_landscape({River(): 0.6, Plain(): 0.4})

    def get_local_map(self):
        tile = self.tiles[self.selected_tile[0]][self.selected_tile[1]]
        if tile.lower_map is None:
            tile.lower_map = Map(100, 100, map_type=get_next_map_type(self.map_type))
        return tile.lower_map

    #     self.tiles[10][20].objects.append(MapObject('Test', 'Test Description', tcod.cyan, '@'))
    # for x in range(self.width):
    #     for y in range(self.height):
    #         if (5 < x < 25) and (5 < y < 25):
    #             1 + 1
    #             self.tiles[10][20].objects.append(MapObject('Test', 'Test Description', tcod.COLOR_CYAN, '@'))

    # for test purposes
    # self.prepare_test_requisites()
    # self.tiles[17][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][17]))
