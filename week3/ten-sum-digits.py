#!/usr/bin/env python3

i = 1
sum = 0
c = 0
d = 0

while i <= 10:
  a = int(input())
  if a > 99:
    a = a % 100 % 10
  elif a >= 0:
    a = a % 10
  else:
    if a > -10:
      a = -a
    else:
      a = -(a + 10)

  sum += a
  i += 1

print(sum)
