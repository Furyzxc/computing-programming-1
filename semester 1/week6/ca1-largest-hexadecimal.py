#!/usr/bin/env python3

n1 = input()
n2 = input()

if len(n1) > len(n2):
  print(n1)
elif len(n2) > len(n1):
  print(n2)
else:
  if n1 > n2:
    print(n1)
  else:
    print(n2)
