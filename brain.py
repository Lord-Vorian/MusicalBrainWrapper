"""
Interfaces with OpenBCI Cyton board for live stream EEG data
"""

from pyOpenBCI import cyton

board = cyton.OpenBCICyton(port='COM3')

def print_raw(sample):
    print(sample.channels_data)


board.start_stream(print_raw)