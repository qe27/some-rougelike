import tcod

import global_variables
from objects.game_objects.world_map.world_map_object import WorldMapObject


class Ship(WorldMapObject):

    def __init__(self, hp, defence, model, max_speed):
        super(WorldMapObject, self).__init__()
        self.max_hp = hp
        self.current_hp = hp
        self.defence = defence
        self.model = model
        self.max_speed = max_speed
        self.current_speed = max_speed
        self.wm_location = None
        self.char = 'S'
        self.color = tcod.red
        self.direction = None

    def set_tile(self, tile):
        self.wm_location = (float(tile.x), float(tile.y))
        tile.objects.append(self)
        self.tile = tile

    def calculate_next_hour(self):
        if self.direction:
            # self.wm_location += tuple([self.current_speed * x for x in self.direction])
            self.wm_location = (self.wm_location[0] + self.current_speed * self.direction[0],
                                self.wm_location[1] + self.current_speed * self.direction[1])
            if self.tile.x != int(self.wm_location[0]) or self.tile.y != int(self.wm_location[1]):
                self.tile.objects = []
                self.tile = self.tile.upper_map.tiles[int(self.wm_location[0])][int(self.wm_location[1])]
                self.tile.objects.append(self)

    def go_to_ship_map(self):
        global_variables.CurrentActiveState.ACTIVE_STATE = global_variables.ActiveStates.SHIP_MAP

    def get_subject_funcs(self):
        results = {}
        if global_variables.player.ship == self:
            results["Go to ship map"] = self.go_to_ship_map
        return results
        # return {"Go to ship map": go_to_ship_map}
