#!/usr/bin/env python3

sumPos = 0
sumNeg = 0
i = 0

while i < 5:
  s = int(input())

  if s < 0:
    sumNeg += s
  else:
    sumPos += s
  i += 1

print(sumNeg, sumPos)
