#!/usr/bin/env python3

s = input()
count = 0

while s != "end":
  if int(s.split()[2]) > 1:
    print(s)
  s = input()
