#!/usr/bin/env python3

import sys

factors = sys.argv[1:]
nums = sys.stdin.read().split()

i = 0

while i < len(nums):
  num = int(nums[i].rstrip())
  j = 0
  while j < len(factors):
    factor = int(factors[j].rstrip())
    if int(num / factor) != num / factor:
      j = len(factors)
    j += 1
  if j == len(factors):
    print(num)
  i += 1
