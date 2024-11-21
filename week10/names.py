#!/usr/bin/env python3

import sys

names = {}

with open("boys.txt") as f:
  curr_names = f.read().split()

  i = 0

  while i < len(curr_names):
    name = curr_names[i]

    names[name] = "boy"
    i += 1

with open("girls.txt") as f:
  curr_names = f.read().split()

  i = 0

  while i < len(curr_names):
    name = curr_names[i]

    if name not in names:
      names[name] = "girl"
    else:
      names[name] = "either"
    i += 1

entered_names = sys.stdin.read().split()

i = 0

while i < len(entered_names):
  curr = entered_names[i]

  if curr in names:
    curr += " " + names[curr]
  else:
    curr += " either"
  print(curr)
  i += 1
