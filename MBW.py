"""
12-22-2018 Lord Vorian

Take inputs from signaler.py and use it to play songs from vibe_parser.py
"""
############################## Imports ########################################
import csv, signaler, vlc
from time import time, sleep
from random import random, choice
from os import path
from  vibe_parser import WORKING_DIR


############################### Get Filenames #################################
cleaned_list = []

with open(path.join(WORKING_DIR,'tempo_list.csv'), 'r') as unread_file:
  read_file = csv.reader(unread_file)
  for line in read_file:
    # ignore blank lines and only fast music!
    if len(line) > 1 and float(line[1]) > 120:
        cleaned_list.append(line)

cleaned_list = sorted(cleaned_list, key=lambda i: float(i[1]), reverse=True)


############################# Set Up timer & listen to signaler ###############

def fadeIn(player, seconds):
  """
  Fade in the song in 1% increments
  :param player: VLC Instance media_player_new
  :param seconds: Time to fade over
  :return: Nothing
  """
  player.audio_set_volume(0)
  player.play()
  seconds = float(seconds)
  step = seconds / 100
  while seconds > 0:
    player.audio_set_volume(100 - int(seconds/step))
    seconds -= step
    sleep(step)


def fadeOut(player, seconds):
  """
  Fade in the song in 1% increments
  :param player: VLC Instance media_player_new
  :param seconds: Time to fade over
  :return: Nothing
  """
  seconds = float(seconds)
  step = seconds / 100
  while seconds > 0:
    player.audio_set_volume(int(seconds/step))
    seconds -= step
    sleep(step)
  player.stop()



def test(player):
  elapsed = 0 # not used, for timeout on test function?
  invasions = 0
  invading = 0
  while True:
    # TODO loop chill bpm
    if not int(time()) % 5:

      if signaler.invader_detect():
        if invading <= 0:
          player.set_media(instance.media_new(choice(cleaned_list)[0]))
          fadeIn(player, 2)
          print('New invasion # {}'.format(invasions))
          invasions += 1
        else:
          invading = 2
      else:
        invading -= 1

      if invading > 0 and not player.is_playing():
        player.set_media(instance.media_new(choice(cleaned_list)[0]))
        fadeIn(player, 1)
      
      elif invading <= 0 and player.is_playing():
        fadeOut(player, 5)
    sleep(1)


if __name__ == "__main__":
  instance = vlc.Instance()
  player = instance.media_player_new()
  sleep(15)
  test(player)