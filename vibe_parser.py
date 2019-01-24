"""
12-5-2018  Lord Vorian
This doc pulls data from music files and prepares them for access
"""

import signaler
import os, csv, getpass, time
import librosa


topPath = 'C:\\Users\\Vorian\\Music'


def get_files():
  """Take a given path and retun absolute path of all supported music files"""
  file_list = []
  csv_cleaned = []
  csv_reader = []
  if os.path.isdir(os.path.join('data', getpass.getuser(),'tempo_list.csv')):
    file = open(os.path.join('data', getpass.getuser(),'tempo_list.csv'),'r')
    csv_reader = csv.reader(file)

  for row in csv_reader:
    if row:
      csv_cleaned.append(row)
  print(csv_cleaned)
  for abspath, intermediate, file_names in os.walk(topPath):
    if file_names:
      for file_name in file_names:
        if os.path.splitext(file_name)[-1] == '.mp3' and \
          file_name not in [row[0] for row in csv_cleaned]:  # TODO add other filetypes
          file_list.append(os.path.join(abspath, file_name))


  return file_list


def get_bpm_list(file_list):
  """
  Compute BPM of each given file and return
  list of [file, bpm, beat times (in seconds)]
  """
  bpm_labels = [] # TODO Only process new files

  for file in file_list:
    #Y is time series, sr is sample rate
    y, sr = librosa.load(file)
    bpm, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    #beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    bpm_labels.append([file, int(bpm)])

  return bpm_labels


def csv_generator(data):
  """Create and maintain reference file for users music library"""
  working_dir = os.path.join('data', getpass.getuser())

  if not os.path.isdir(working_dir):
    os.mkdir(os.path.abspath(working_dir))

  with open(os.path.join(working_dir,'tempo_list.csv'), 'w') as write_file:
    writer = csv.writer(write_file)  # TODO add header for reading as table
    for row in data:
      writer.writerow(row)



def test(file_list):
  start = time.time()
  thing = get_bpm_list(file_list)
  end = time.time()
  print("took {} secs".format(int(end-start)))
  return thing
