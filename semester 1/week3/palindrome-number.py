#!/usr/bin/env python3

a = 0
num = int(input())
c = num
while num > 0:
  r = num % 10
  num = num // 10
  a = (10 * a) + r
if a == c:
  print('yes')
else:
  print('no')
