from objects.game_objects.ship.ship_tile import ShipTile


class ShipLayer:

    def __init__(self, tiles):
        self.tiles = tiles
        for x in range(len(self.tiles[0])):
            for y in range(len(self.tiles)):
                self.tiles[y][x].layer = self


def read_model_from_file(file):
    return
