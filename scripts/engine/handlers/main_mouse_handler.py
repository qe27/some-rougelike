import global_variables
from global_variables import *
from rendering.screen_options import *


def handle_mouse(mouse):
    if 0 <= mouse.cx < SCREEN_WIDTH - PANEL_WIDTH and 0 <= mouse.cy < MAP_PANEL_HEIGHT:
        print('mouse x: %d         mouse y: %d' % (mouse.cx, mouse.cy))
        global_variables.selected_tile = (mouse.cx, mouse.cy)
    elif SCREEN_WIDTH - 10 <= mouse.cx <= SCREEN_WIDTH and \
            SCREEN_HEIGHT - 3 <= mouse.cy <= SCREEN_HEIGHT:
        print('pressed end turn button!!!')
    elif SCREEN_WIDTH - PANEL_WIDTH <= mouse.cx <= SCREEN_WIDTH and \
            A_PANEL_HEIGHT <= mouse.cy <= A_PANEL_HEIGHT + M_PANEL_HEIGHT:
        selected_option = mouse.cy - A_PANEL_HEIGHT
        if global_variables.tile_info_options[selected_option]:
            print('selected option: ' + global_variables.tile_info_options[selected_option].name)
            global_variables.selected_object = global_variables.tile_info_options[selected_option]
    elif MAP_PANEL_HEIGHT <= mouse.cy <= SCREEN_HEIGHT:
        if global_variables.object_options.get(mouse.cy - MAP_PANEL_HEIGHT):
            global_variables.object_options[mouse.cy - MAP_PANEL_HEIGHT]()