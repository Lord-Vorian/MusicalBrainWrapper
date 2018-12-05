import os

topPath = '/home/blandon/Music'


def get_files():
    file_list = []
    for abspath, intermediate, file_names in os.walk(topPath):
        if file_names:
            for file_name in file_names:
                if os.path.splitext(file_name)[-1] == '.mp3':
                    file_list.append(os.path.join(abspath, file_name))
    return file_list

