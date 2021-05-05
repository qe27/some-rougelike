import global_variables
from global_variables import *
from rendering.screen_options import *


def handle_mouse(mouse):
    current_map = global_variables.get_current_map()
    if 0 <= mouse.cx < SCREEN_WIDTH - PANEL_WIDTH and 0 <= mouse.cy < MAIN_PANEL_HEIGHT:
        print('mouse x: %d         mouse y: %d' % (mouse.cx, mouse.cy))
        current_map.selected_tile = (mouse.cx + map_offset[0], mouse.cy + map_offset[1])
    elif SCREEN_WIDTH - 10 <= mouse.cx <= SCREEN_WIDTH and \
            SCREEN_HEIGHT - 3 <= mouse.cy <= SCREEN_HEIGHT:
        print('pressed end turn button!!!')
    elif SCREEN_WIDTH - PANEL_WIDTH <= mouse.cx <= SCREEN_WIDTH and \
            A_PANEL_HEIGHT <= mouse.cy <= A_PANEL_HEIGHT + M_PANEL_HEIGHT:
        selected_option = mouse.cy - A_PANEL_HEIGHT
        if global_variables.tile_info_options[selected_option]:
            print('selected option: ' + global_variables.tile_info_options[selected_option].name)
            global_variables.selected_object = global_variables.tile_info_options[selected_option]
    elif MAIN_PANEL_HEIGHT <= mouse.cy <= SCREEN_HEIGHT:
        if global_variables.object_options.get(mouse.cy - MAIN_PANEL_HEIGHT):
            global_variables.object_options[mouse.cy - MAIN_PANEL_HEIGHT]()