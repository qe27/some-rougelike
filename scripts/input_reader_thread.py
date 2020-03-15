from threading import Thread
import tcod as libtcod


class InputReaderThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.key_pressed = None

    def run(self):
        key = libtcod.Key()
        mouse = libtcod.Mouse()
        while not libtcod.console_is_window_closed():
            libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS | libtcod.EVENT_MOUSE, key, mouse)
            if key.c is not None:
                self.key_pressed = key
