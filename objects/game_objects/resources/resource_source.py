from objects.game_objects.resources import resources_types


class ResourceSource:

    def __init__(self, name=None, resource_type=None, initial_quantity=1000,
                 quantity_remains=1000, terrain=None):
        self.name = name
        if resource_type:
            self.resource_type = resource_type
            self.renewable = resources_types.RESOURCES_DICT.get(resource_type).get('renewable')
            self.renewable_rate = resources_types.RESOURCES_DICT.get(resource_type).get('renewable_rate')
        self.initial_quantity = initial_quantity
        self.quantity_remains = quantity_remains
        self.terrain = terrain
