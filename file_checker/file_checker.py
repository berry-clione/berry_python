# support python3

import os
import datetime
import csv
from chardet.universaldetector import UniversalDetector

_path = './file/'

# get encode of a file
def univ_detect(file_dir):
    ud = UniversalDetector()
    with open(file_dir, 'rb') as fd:
        for b in fd:
            ud.feed(b)
            if ud.done:
                break
    ud.close()
    return ud.result['encoding']

# get a file name, path and last-modified timestamp
all_files = []
def get_file_list(file_path):
    # all_files = []
    file_list = [f for f in os.listdir(file_path)]
    for g in file_list:
        g_path = os.path.join(file_path, g)

        # last modified time        
        last_modified = os.path.getmtime(g_path)
        dt = datetime.datetime.fromtimestamp(last_modified).strftime('%Y%m%d_%H:%M:%S')

        # chardet
        encode = 'Directory'
        if os.path.isdir(g_path):
            pass
        else:
            encode = univ_detect(g_path)

        all_files.append([dt, g_path.split(_path,1)[1], ' '.join(['~',encode,'~'])])

        # subdirectory
        if os.path.isdir(g_path):
            subfile_list = [i for i in os.listdir(g_path)]
            for j in subfile_list:
                j_path = os.path.join(g_path, j)

                # last modified time
                sub_last_modified = os.path.getmtime(j_path)
                sub_dt = datetime.datetime.fromtimestamp(sub_last_modified).strftime('%Y%m%d_%H:%M:%S')

                # chardet
                encode = 'Directory'
                if os.path.isdir(j_path):
                    pass
                else:
                    encode = univ_detect(j_path)

                all_files.append([sub_dt, j_path.split(_path,1)[1], ' '.join(['~',encode,'~'])])
    return file_list
    # return all_files

print(get_file_list(_path))

csv_file = [['Last_modified', 'file_path', 'encode']] # Header
csv_file.extend(all_files)
with open('file_checker.csv', 'w') as h:
    writer = csv.writer(h, lineterminator='\n')
    writer.writerows(csv_file)
