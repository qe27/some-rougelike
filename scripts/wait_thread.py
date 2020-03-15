import time
from threading import Thread


class WaitThread(Thread):

    def __init__(self, wait_time):
        Thread.__init__(self)
        self.wait_time = wait_time

    def run(self):
        time.sleep(self.wait_time)
