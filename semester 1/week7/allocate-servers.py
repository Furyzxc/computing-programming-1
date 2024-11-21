#!/usr/bin/env python3

a = []

s = input()

while s != "end":
  a.append(int(s))
  s = input()

i = 0

max = 0

while i < len(a) - 1:
  j = i + 1
  servers = 1
  while j < len(a) and a[i] + 1000 > a[j]:
    servers += 1
    j += 1
  if servers > max:
    max = servers
  i += 1

print(max)
