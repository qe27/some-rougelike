class ExplodeAction:

    def __init__(self):
        return

    def action(self, tile, tiles):
        objs = tiles[tile.x][tile.y].objects
        if len(objs) > 1:
            print('test')
        return
