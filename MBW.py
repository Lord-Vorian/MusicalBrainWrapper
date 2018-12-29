"""
12-22-2018 Lord Vorian

Take inputs from signaler.py and use it to play songs from vibe_parser.py
"""

from pygame import mixer

with open('tempo_list.csv') as file:
  for i in file:
    print(i)

# song = mixer.music.load()