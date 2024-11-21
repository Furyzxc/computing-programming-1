#!/usr/bin/env python3

s = input()

n = -1

i = 0
while i < len(s):
  if "0" <= s[i] <= "9":
    n = s[i]
  i += 1


if n != -1:
  print(n)
