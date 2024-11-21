#!/usr/bin/env python3

odd = []

s = input()

while s != "end":
  if int(s) % 2 == 0:
    print(s)
  else:
    odd.append(s)
  s = input()

i = 0

while i < len(odd):
  print(odd[i])
  i += 1
