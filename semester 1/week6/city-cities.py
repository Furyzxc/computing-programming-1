#!/usr/bin/env python3

s = input()

while s != "end":
  i = 4

  while i < len(s) and s[i - 4:i] != "City":
    i += 1
  if i != len(s) and i - 4 != 0:
    print(s[:i])
  s = input()
