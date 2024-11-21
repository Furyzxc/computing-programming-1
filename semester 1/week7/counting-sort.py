#!/usr/bin/env python3

a = 999 * [0]

s = input()

while s != "end":
  a[int(s)] += 1
  s = input()

i = 0

while i < len(a):
  if a[i] > 0:
    print(a[i] * (str(i) + "\n"), end="")
  i += 1
