#!/usr/bin/env python3

x1 = int(input())
y1 = int(input())

r = int(input())

x2 = int(input())
y2 = int(input())

inCircle = r * r - ((x1 - x2) ** 2 + (y1 - y2) ** 2) > 0

if inCircle:
  print("yes")
else:
  print("no")
