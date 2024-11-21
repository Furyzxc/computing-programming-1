#!/usr/bin/env python3

sum = 0

i = 0

while i < 5:
  s = int(input())

  if s < 0:
    sum += -1 * s
  else:
    sum += s
  i += 1

print(sum)
