import tcod

from objects.game_objects.structures.structure import Structure


class Settlement(Structure):
    type = 'Settlement'

    def __init__(self, name='Moscow', description='Test Description', color=tcod.red, char=None, options={}):
        super(Structure, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = 'S'
        self.population = options.get('population')
        self.type = 'Settlement'
        self.buildings = []

    def end_turn(self):
        print('end turn for settlement')