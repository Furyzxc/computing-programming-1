#!/usr/bin/env python3

import os

unvisited = ["."]

while len(unvisited) > 0:
  curr = unvisited.pop()

  files = os.listdir(curr)

  i = 0
  while i < len(files):
    file = curr + "/" + files[i]
    if os.path.isfile(file):
      print(file)
    elif os.path.isdir(file):
      unvisited.append(file)
    i += 1
