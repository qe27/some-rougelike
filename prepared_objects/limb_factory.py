from objects.game_objects.unit.body_state import ManipulationLimb


def createHand(prefix):
    return ManipulationLimb(name=prefix + 'Hand', fingers=5)
