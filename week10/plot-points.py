#!/usr/bin/env python3

import sys

print(" --------------------")
line = sys.stdin.readline()

cords = {}

result = ""

while line:

  cords[line.strip()] = True
  line = sys.stdin.readline()


y = 0

while y < 20:
  line = "|"
  x = 0
  while x < 20:
    if str(x) + " " + str(y) in cords:
      line += "*"
    else:
      line += " "
    x += 1
  line += "|"

  result += line[::-1]
  if y != 19:
    result += "\n"

  y += 1

print(result[::-1])
print(" --------------------")
