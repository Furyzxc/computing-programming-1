#!/usr/bin/env python3

i = 0

s = ""
str = input()

while i < len(str):
  s += str[i].capitalize()
  i += 1

print(s)
