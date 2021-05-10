from objects.game_objects.ship.ship_tile import ShipTile


class ShipLayer:

    def __init__(self, tiles):
        self.tiles = tiles
        self.height = len(self.tiles)
        self.width = len(self.tiles[0])
        self.selected_tile = None
        for x in range(self.width):
            for y in range(self.height):
                self.tiles[y][x].layer = self


def read_model_from_file(file):
    return
