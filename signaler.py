"""
12/7/2018 Lord Vorian
This module(?) carries all of the monitoring functionality
"""
from pyautogui import screenshot

def invader_detect():
  """Takes a screen and looks for red clumps"""
  image = screenshot()
  red_count = 0
  total = 0
  for pixel in image.getdata():
    total += 1
    if pixel[0] > 160 and pixel[1] < 55 and pixel[2] < 60:
      red_count += 1
  image.save('temp.png')
  print("""Red pixels:{}\nout of: {}\nPercent red:%{:.2f}""".format(red_count,total,red_count/total*100))
  if red_count > 4000:
    print('Red detected')
