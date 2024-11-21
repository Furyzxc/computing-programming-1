#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0

while i < len(files):
  file = files[i]
  arr = file.split(".")
  if len(arr) >= 3 and arr[-1] == "bak":
    os.unlink(file)
  i += 1
