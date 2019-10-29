"""
Interfaces with OpenBCI Cyton board for live stream EEG data
"""

from pyOpenBCI import cyton
import signaler
import threading


board = cyton.OpenBCICyton(port='COM3')

class Streamer:

    def __init__(self, flagger):
        self.flag = False
        self.flagger = flagger

    def update_flag(self):
        flagger = threading.Thread(target=self.flagger.blink)


def print_raw(sample):
    print(sample.channels_data)


board.start_stream(print_raw)