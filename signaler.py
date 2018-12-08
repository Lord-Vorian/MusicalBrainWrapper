"""
12/7/2018 Lord Vorian
This module(?) carries all of the monitoring functionality
"""
from pyautogui import screenshot
from time import time, sleep

def invader_detect():
  """Takes a screen and looks for red clumps"""
  image = screenshot()
  red_count = 0
  pink_count = 0
  total = 0
  for pixel in image.getdata():
    total += 1
    if pixel[0] > 160 and pixel[1] < 55 and pixel[2] < 60:
      red_count += 1

    elif pixel[0] > 150 and pixel[1] < 50 and pixel[2] > 150:
      pink_count += 1

  image.save('temp.png')
  if red_count > 1000:
    print('Red Invader detected')
  if pink_count > 50:
    print('Pink Invader detected')


def blink():
  """Run detection func at a set time interval"""
  elapsed = 0
  while elapsed < 3600:
    elapsed += 1
    if not int(time())%5:
      invader_detect()
    sleep(1)