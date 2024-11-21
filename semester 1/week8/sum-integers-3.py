#!/usr/bin/env python3

import sys

files = sys.argv[1:]
i = 0
sum = 0
while i < len(files) != "":
  with open(files[i]) as f:
    a = f.readline()
    while a != "":
      sum += int(a)
      a = f.readline()
  i += 1
print(sum)
