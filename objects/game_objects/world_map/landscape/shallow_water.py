import tcod

from objects.game_objects.world_map.world_map_object import WorldMapObject


class ShallowWater(WorldMapObject):
    type = 'settlement'

    def __init__(self, name='Shallow Water', description='This is a shallow water', color=tcod.light_azure, char=None, options={}):
        super(WorldMapObject, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = '~'
        self.type = ShallowWater.type
