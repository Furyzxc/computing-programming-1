#!/usr/bin/env python3

i = 1
sum = 0

while i <= 10:
  a = int(input())

  if a < sum:
    sum = a

  i += 1

print(sum)
