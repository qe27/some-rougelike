import tcod

from map_objects.tile import Tile
from objects.game_objects.landscape.plain import Plain
from objects.game_objects.landscape.river import River
from objects.game_objects.map_object import MapObject


class WorldMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()
        self.make_map()

    def initialize_tiles(self):
        tiles = [[Tile(self, x, y) for y in range(self.height)] for x in range(self.width)]
        return tiles

    def make_map(self):
        for x in range(self.width):
            for y in range(self.height):
                if (x == 10) or (y == 15):
                    self.tiles[x][y].tile_structure.set_landscape({River(): 0.6, Plain(): 0.4})

    #     self.tiles[10][20].objects.append(MapObject('Test', 'Test Description', tcod.cyan, '@'))
        # for x in range(self.width):
        #     for y in range(self.height):
        #         if (5 < x < 25) and (5 < y < 25):
        #             1 + 1
        #             self.tiles[10][20].objects.append(MapObject('Test', 'Test Description', tcod.COLOR_CYAN, '@'))

        # for test purposes
        # self.prepare_test_requisites()
        # self.tiles[17][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][17]))