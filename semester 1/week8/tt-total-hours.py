#!/usr/bin/env python3

s = input()
count = 0

while s != "end":
  count += int(s.split()[2])
  s = input()

print(count)
