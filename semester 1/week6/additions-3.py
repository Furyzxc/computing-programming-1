#!/usr/bin/env python3


total = 0

while total != 1000:
  j = 0
  s = input()

  while s[j] != "+":
    j += 1

  total = int(s[:j]) + int(s[j + 1::])

  print(total)
