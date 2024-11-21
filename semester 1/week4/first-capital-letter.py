#!/usr/bin/env python3

str = input()
i = 0
ch = str[i]

while not (65 <= ord(ch) and ord(ch) <= 90):
  i += 1
  ch = str[i]

print(i)
