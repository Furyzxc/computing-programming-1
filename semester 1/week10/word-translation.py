#!/usr/bin/env python3

import sys

dict = {}

with open("translation.txt") as f:
  line = f.readline().rstrip().split()
  while len(line) > 0:
    dict[line[0]] = line[1]
    line = f.readline().rstrip().split()

words = sys.stdin.read().split()

i = 0

while i < len(words):
  print(dict[words[i]])
  i += 1
