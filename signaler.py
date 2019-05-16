"""
12/7/2018 Lord Vorian
This module(?) carries all of the monitoring functionality
"""
from pyautogui import screenshot
from time import time, sleep

def invader_detect():
  """Takes a screenshot and looks for red clumps"""
  image = screenshot()
  red_count = 0
  pink_count = 0
  total = 0 # not used
  for pixel in image.getdata():
    total += 1 # not used
    if pixel[0] > 100 and pixel[1] < 50 and pixel[2] < 50:
      red_count += 1

    elif pixel[0] > 100 and pixel[1] < 50 and pixel[2] > 150:
      pink_count += 1

  image.save('temp.png')
  if red_count > 1000:
    print('Red Invader detected')
    return True
  elif pink_count > 50:
    print('Pink Invader detected')
    return True
  else:
    return False

def blink(interval=3600):
  """Run detection func at a set time interval"""
  for elapsed in range(interval):
    if not (int(time()) % 5): invader_detect()
    sleep(1)