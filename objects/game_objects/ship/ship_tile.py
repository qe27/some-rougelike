class ShipTile:

    def __init__(self, x, y, layer=None, tile_type=None, material=None):
        self.x = x
        self.y = y
        self.layer = layer
        self.material = material
        self.type = tile_type
        # self.flammable = material.flamable
        # self.durability = material.durability
        # self.density = material.density
