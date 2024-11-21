#!/usr/bin/env python3

s = input()

i = 0

found = True

while i < len(s) - 1 and s[i] != s[i + 1]:
  if i == len(s) - 1:
    found = False
  i += 1

if found and i + 1 < len(s):
  print(s[i] + s[i + 1])
