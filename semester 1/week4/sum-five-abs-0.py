#!/usr/bin/env python3

sum = 0

s = 1

while s != 0:
  s = int(input())

  if s < 0:
    sum += -1 * s
  else:
    sum += s

print(sum)
