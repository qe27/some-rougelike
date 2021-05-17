import tcod

from objects.game_objects.world_map.world_map_object import WorldMapObject


class Settlement(WorldMapObject):
    type = 'settlement'

    def __init__(self, name='Settlement', description='This is a settlement', color=tcod.yellow, char=None, options={}):
        super(WorldMapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = 'S'
        self.type = Settlement.type
