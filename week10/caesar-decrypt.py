#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

dict = {}
n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

i = 0

while i < len(dst):
  dict[dst[i]] = src[i]
  i += 1

while line != "":
  stripped = line.strip()

  new_line = ""

  i = 0

  while i < len(stripped):
    char = stripped[i]

    if char in dict:
      new_line += dict[char]
    else:
      new_line += char
    i += 1
  print(new_line)

  line = sys.stdin.readline()
