#!/usr/bin/env python3

str = input()
i = 0
ch = str[i]

while not (97 <= ord(ch) and ord(ch) <= 103):
  i += 1
  ch = str[i]

print(ch)
