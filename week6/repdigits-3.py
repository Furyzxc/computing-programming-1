#!/usr/bin/env python3

s = input()
count = True

while s != "end":
  if count and s[0] == s[1]:
    print(s)
    count = False
  s = input()
