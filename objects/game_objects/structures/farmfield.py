import tcod

from objects.game_objects.structures.structure import Structure
from objects.production.production import ProductionSite


class Farmfield(Structure, ProductionSite):
    type = 'Farmfield'

    def __init__(self, name='Crop field', description='Big field with a scarecrow', color=tcod.red, char=None, options={}):
        super(Structure, self).__init__()
        super(ProductionSite, self).__init__()
        self.name = name
        self.description = description
        self.color = color
        self.options = options
        self.char = '\''
        self.size = 10
        self.type = 'Farmfield'
        self.production = options.get('production')

    def end_turn(self):
        self.do_production_for_turn()
