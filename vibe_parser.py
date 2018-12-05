"""
12-5-2018  Lord Vorian
This doc pulls data from music files and prepares them for access
"""


import os, csv, getpass, time
import librosa

topPath = 'C:\\Users\\Vorian\\Music'


def get_files():
  """Take a given path and retun absolute path of all supported music files"""
  file_list = []
  for abspath, intermediate, file_names in os.walk(topPath):
    if file_names:
      for file_name in file_names:
        if os.path.splitext(file_name)[-1] == '.mp3':
          file_list.append(os.path.join(abspath, file_name))
  return file_list


def get_bpm_list(file_list):
  """
  Compute BPM of each given file and return
  list of [file, bpm, beat times (in seconds)]
  """
  bpm_labels = [] # todo Only process new files
  for file in file_list:
    #Y is time series, sr is sample rate
    y, sr = librosa.load(file)
    bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    bpm_labels.append([file, bpm, beat_times])

  return bpm_labels


def csv_generator(data):
  """Create and maintain reference file for users music library"""
  working_dir = os.path.join('data', getpass.getuser())
  if not os.path.isdir(working_dir):
    os.mkdir(working_dir)
  with open(os.path.join(working_dir, 'tempo_list.csv'), 'w') as write_file:
    writer = csv.writer(write_file)
    writer.writerows(data)


def test():
  start_time = int(time.time())
  file_list = get_files()
  print('{} seconds to get list of files'.format(int(time.time())-start_time))
  start_time = int(time.time())
  bpm_labels = get_bpm_list(file_list)
  print('{} seconds to get bpm of files'.format(int(time.time())-start_time))
  start_time = int(time.time())
  csv_generator(bpm_labels)
  print('{} seconds to write csv'.format(int(time.time())-start_time))
