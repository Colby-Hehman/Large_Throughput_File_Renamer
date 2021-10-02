'''
This program is used to rename files en masse easily. You provide the name you want each file to have,
and they will all be renamed with that phrase as well as number. For example, if you selected 12 files and the phrase
"Hello", then they would all be renamed "Hello (1)" though "Hello (12)". You can already sort of do this in Windows
10, but that uses the same number for file formats. For instance, instead of "Hello (1).png, Hello (2).png,
Hello (3).jpg" you would get "Hello (1).png, Hello (1).jpg, Hello (2).png" which is very annoying.

This program is also useful because it is highly customizable. You can start off at any number, and also customize
how the number is presented. This makes the program much better than the Windows 10 system for renaming lots of files
at once.
'''
import os
from tkinter.filedialog import askopenfilenames
from os import listdir
from os.path import isfile, join


def rename_files(new_name, starting_idx=1, idx_front=' (', idx_back=')'):
    filepaths = list(askopenfilenames())
    for idx, path in enumerate(filepaths):
        filepaths[idx] = path.split(path[path.rindex(".")])
    for path in filepaths:
        path0 = path[0]
        last_slash = path0.rindex("/")
        directory = path0[:last_slash]
        directory = directory.replace('/', '\\')
        dir_files = [f for f in listdir(directory) if isfile(join(directory, f))]
        for idx, file in enumerate(dir_files):
            dir_files[idx] = file[:file.rindex(".")]
        dir_files = set(dir_files)
        idx = starting_idx
        while True:
            if new_name + idx_front + str(idx) + idx_back not in dir_files:
                if idx == starting_idx + len(filepaths):
                    break
                new_path = path0[:last_slash + 1] + new_name + idx_front + str(idx) + idx_back + '.' + path[1]
                os.rename(path[0] + '.' + path[1], new_path)
                break
            else:
                idx += 1


# Here you may call rename_files().  If you want default everything, then just fill the one parameter "new_name"
# which is the name each file will be changed to.


# After that, if you'd like, you can also fill in the number you'd like to start at. The next two parameters after
# that are the text that wrap around the number. Default for the idx_front is " (" and default for the idx_back is
# ")". If the index we were at was 1, then this is how it would be formatted: "File name (1)". If you'd like it to be
# changed to something like "File name-1", then enter "-" for the idx_front and "" for the idx_back.




