#!/usr/bin/env python3

i = 0
sum = 0
d = 0

while i < 10:
  sum += int(input()) * 10 ** i

  i += 1
i = 9

while i >= 0:
  d = sum // 10 ** i
  print(d)
  sum = sum % 10 ** i
  i -= 1
