#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0

while i < len(files):
  if files[i].split(".")[-1] != "bak":
    f1 = open(files[i])
    data = f1.readline()
    f = open(files[i] + ".bak", "w")
    while data != "":
      f.write(data)
      data = f1.readline()
    f1.close()
    f.close()
  i += 1
