#!/usr/bin/env python3

with open("input.txt") as f:
  string = ""
  s = f.read(1)
  while 0 < len(s):
    string += s
    s = f.read(1)
  print(string[:-1])
