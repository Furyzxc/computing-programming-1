#!/usr/bin/env python3

import os

all_files = os.listdir(".")

i = 0

while i < len(all_files):
  file = all_files[i]

  if os.path.isdir(file):
    directory = "./" + file

    directories = os.listdir(directory)

    j = 0
    while j < len(directories) and os.path.isdir(directories[j]):
      curr_files = os.listdir(directory)
      directories[j] = directories[j] + "/" + curr_files[j]
      j += 1
    print(directories)
  else:
    print("./" + file)
  i += 1
