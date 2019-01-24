"""
12-5-2018  Lord Vorian
This doc pulls data from music files and prepares them for access
"""

import signaler
import os, csv, getpass, time
import librosa


TOP_PATH = 'C:\\Users\\Vorian\\Music'
WORKING_DIR = os.path.join('data', getpass.getuser())


def get_files():
  """
  Take a given path and return absolute path of all supported and new
  music files.
  """
  file_list = []
  new_tracks = []
  csv_current = []
  working_dir = os.path.join('data', getpass.getuser())

  for abspath, intermediate, file_names in os.walk(TOP_PATH):
    if file_names:
      for file_name in file_names:
        if os.path.splitext(file_name)[-1] == '.mp3':  # TODO add other filetypes
          file_list.append(os.path.join(abspath, file_name))

  if os.path.isdir(working_dir):
    with open(os.path.join(working_dir,'tempo_list.csv'),'r')as old:
      old_reader = csv.reader(old)

    # check if old csv has tracks that have since been deleted
      for row in old_reader:
        if len(row) > 1:  # filter out empty rows
          if row[0] in file_list:
            csv_current.append(row)


      # check for any tracks that have been added
      for row in file_list:
        if row not in [row[0] for row in csv_current]:
          new_tracks.append(row)

    return csv_current, new_tracks

  else:
    print("No csv detected")
    return [], file_list




def get_bpm_list(new_tracks):
  """
  Compute BPM of each given file and return
  list of [file, bpm, beat times (in seconds)]
  """
  bpm_labels = [] # TODO Only process new files

  for file in new_tracks:
    #Y is time series, sr is sample rate
    y, sr = librosa.load(file)
    bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    #beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    bpm_labels.append([file, int(bpm)])

  return bpm_labels


def csv_generator(current, new_labels):
  """Create and maintain reference file for users music library"""
  working_dir = os.path.join('data', getpass.getuser())
  current.extend(new_labels)
  if not os.path.isdir(working_dir):
    os.mkdir(os.path.abspath(working_dir))

  with open(os.path.join(working_dir,'tempo_list.csv'), 'w') as write_file:
    writer = csv.writer(write_file)  # TODO add header for reading as table
    for row in current:
      writer.writerow(row)


def test():
  current, new = get_files()
  start = time.time()
  new_labels = get_bpm_list(new)
  end = time.time()
  print("took {} secs".format(int(end-start)))
  csv_generator(current, new_labels)

