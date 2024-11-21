#!/usr/bin/env python3

a = int(input())

b = a == 11 or a == 12 or a == 13 or a == 111
if b or a == 112 or a == 113 or a == 1211 or a == 1212 or a == 1213:
  print('th')
elif a % 10 == 1:
  print('st')
elif a % 10 == 2:
  print('nd')
elif a % 10 == 3:
  print('rd')
else:
  print('th')
