#!/usr/bin/env python3

a = int(input())
b = int(input())
c = a

while b != 0:
  a = b
  b = c % b
  c = a

print(c)
