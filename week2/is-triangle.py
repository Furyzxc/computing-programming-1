#!/usr/bin/env python3

a = int(input())
b = int(input())
c = int(input())

if a - b - c >= 0:
  print('no')
elif b - a - c >= 0:
  print('no')
elif c - b - a >= 0:
  print('no')
else:
  print('yes')
