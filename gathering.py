"""
12-22-2018 Lord Vorian

Take inputs from signaler.py and use it record screen and mark time
"""

import signaler, subprocess
from time import time, sleep




def start_rec():
  subprocess.Popen(["startVLCrec.bat", str(int(time()))])

def stop_rec():
  subprocess.Popen("stopVLCrec.bat")


def test():
  recording = False
  invasions = 0
  invading = 0
  while True:
    if not int(time()) % 5:

      if signaler.invader_detect() and invading <= 0:  # first sighting
        start_rec()
        recording = True
        print('New invasion # {}'.format(invasions))
        invasions += 1
        invading = 2

      elif invading <= 0:
        if recording:
          stop_rec()
          recording = False
        pass
      elif signaler.invader_detect() and invading > 0:  # Regenerate decay
        invading = 2

      elif not signaler.invader_detect():  # decay if unseen
        invading -= 1


    sleep(1)


if __name__ == "__main__":
  sleep(15)
  test()