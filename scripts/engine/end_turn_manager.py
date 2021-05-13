import global_variables


def world_map_next_hour():
    # move player
    # move other ships
    print('next hour started')
    global_variables.player.ship.calculate_next_hour()
