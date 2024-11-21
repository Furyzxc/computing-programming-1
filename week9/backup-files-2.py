#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0

while i < len(files):
  file = files[i]

  if os.path.isfile(file) and file.split(".")[-1] != "bak":
    f = open(file)
    backup_file = open(file + ".bak", "w")

    line = f.readline()

    while line != "":
      backup_file.write(line)
      line = f.readline()

    f.close()
    backup_file.close()
  i += 1
