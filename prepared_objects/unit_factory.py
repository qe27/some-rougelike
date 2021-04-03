import tcod as libtcod

from objects.game_objects.unit.body_state import BodyState
from objects.game_objects.unit.general_unit_object import GeneralUnitObject
from prepared_objects.limb_factory import createHand


def createHuman(name, tile):
    leftHand = createHand('Left')
    rightHand = createHand('Right')
    return GeneralUnitObject(libtcod.red, name, BodyState([leftHand, rightHand]), tile=tile)
