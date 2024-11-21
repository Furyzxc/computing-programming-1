#!/usr/bin/env python3

import sys

ger = "eins zwei drei vier funf sechs sieben acht neun zehn".split()

eng = "one two three four five six seven eight nine ten".split()

dict = {}

i = 0

while i < len(ger) and i < len(eng):
  dict[eng[i]] = ger[i]
  i += 1

nums = sys.stdin.read().split()

i = 0

while i < len(nums):
  print(dict[nums[i].rstrip()])
  i += 1
