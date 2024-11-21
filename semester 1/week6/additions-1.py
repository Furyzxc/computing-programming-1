#!/usr/bin/env python3

i = 0

while i < 10:
  j = 0
  s = input()

  while s[j] != "+":
    j += 1

  print(int(s[:j]) + int(s[j + 1::]))
  i += 1
