#!/usr/bin/env python3

s = input()
count = 0

while s != "end":
  i = 2

  while i < len(s) and s[i - 2:i] != "WI":
    i += 1
  if i != len(s):
    count += 1
  s = input()

print(count)
