#!/usr/bin/env python3

s = input()

while s != "end":
  i = 0

  while s[i] != " " and i < len(s):
    i += 1

  a = s[0:i]
  b = s[i::]

  print(" " * (20 - len(s) - 3) + a + " +" + b + " = " + str(int(a) + int(b)))

  s = input()
