"""
12/7/2018 Lord Vorian
This module(?) carries all of the monitoring functionality
"""
from pyautogui import screenshot
from time import time, sleep
class Signaler:

  def __init__(self):
    self.invader = False

  def invader_detect(self):
    """Takes a screenshot and looks for red clumps"""
    image = screenshot(); image.save('temp.png')
    red_count, pink_count = 0, 0
    total = 0 # not used

    for pixel in image.getdata():
      total += 1 # not used
      if pixel[0] > 100 and pixel[1] < 50:
        if pixel[2] < 50: red_count += 1
        elif pixel[2] > 150: pink_count += 1

      if red_count > 1000:
        print('Red Invader detected')
        return True
      elif pink_count > 25:
        print('Pink Invader detected')
        return True
    return False


  def blink(self, interval=3600):
    """Run detection func at a set time interval"""
    for elapsed in range(interval):
      if not (int(time()) % 5): self.invader = self.invader_detect()
      sleep(1)