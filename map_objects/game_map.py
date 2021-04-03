import tcod as libtcod

from map_objects.tile import Tile
from objects.game_objects.interactable_object import InteractableObject
from prepared_objects.unit_factory import createHuman
from scripts.oob_actions.end_turn_action.explode_action import ExplodeAction
from scripts.oob_actions.stove_test_action import StoveTestAction


class FloorMap:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[Tile(self, x, y) for y in range(self.height)] for x in range(self.width)]

        return tiles

    def make_map(self):
        for x in range(self.width):
            for y in range(self.height):
                if (5 < x < 25) and (5 < y < 25):
                    self.tiles[x][y].exists = True

        # for test purposes
        self.prepare_test_requisites()

    def prepare_test_requisites(self):
        # worker = GeneralUnitObject(libtcod.red, "player2", tile=self.tiles[24][24])
        worker = createHuman("player1", tile=self.tiles[24][24])

        self.tiles[24][24].objects.append(worker)
        self.tiles[17][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][17]))
        self.tiles[18][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[18][17]))
        self.tiles[19][17].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[19][17]))
        self.tiles[11][11].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[11][11]))
        self.tiles[9][11].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[9][11]))
        worker.addAction(add_test_stove(self.tiles[9][10]).action)
        worker.addAction(add_test_stove(self.tiles[16][16]).action)
        self.tiles[14][15].objects.append(InteractableObject(libtcod.green, "Mine", "M", tile=self.tiles[14][15],
                                                             endTurnAction=ExplodeAction(), blocks=False))
        self.tiles[8][11].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[8][11]))
        self.tiles[10][11].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[10][11]))
        self.tiles[11][10].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[11][10]))
        self.tiles[17][12].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][12]))
        self.tiles[17][13].objects.append(InteractableObject(libtcod.green, "Cabinet", "C", tile=self.tiles[17][13]))


def add_test_stove(tile):
    test_stove = InteractableObject(libtcod.white, "Stove", "S", tile=tile)
    test_action = StoveTestAction(test_stove)
    test_stove.action = test_action
    tile.objects.append(test_stove)
    return test_stove


def add_test_mine(tile):
    test_mine = InteractableObject(libtcod.blue, "Mine", "m", tile=tile)
    test_mine.endTurnAction = ExplodeAction()
