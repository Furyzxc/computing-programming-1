#!/usr/bin/env python3

sumPos = 0
sumNeg = 0
s = 1

while s != 0:
  s = int(input())

  if s < 0:
    sumNeg += s
  else:
    sumPos += s

print(sumNeg, sumPos)
