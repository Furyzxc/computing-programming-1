#!/usr/bin/env python3

i = 1
sum = 10000000

while i <= 10:
  a = int(input())

  if a < sum and a % 2 == 0:
    sum = a

  i += 1

print(sum)
