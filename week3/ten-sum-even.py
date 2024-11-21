#!/usr/bin/env python3

i = 0
sum = 0

while i < 10:
  a = int(input())

  if a % 2 == 0:
    sum += a
  i += 1

print(sum)
