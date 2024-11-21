#!/usr/bin/env python3

n = int(input())

x = 0
y = 1
f = 0

i = 0

while i < n:
  if f < n:
    print(f)

  x = y
  y = f

  f = x + y

  i += 1
