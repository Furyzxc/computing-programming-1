#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

total = 0
count = 0

people = []
dict = {}
while line:
  count += 1
  arr = line.strip().split()
  person = " ".join(arr[0:2])
  mark = arr[-1]
  total += int(mark)
  dict[person] = int(mark)
  people += [person]
  line = sys.stdin.readline()

av = total / len(dict)
i = 0
while i < len(people):
  if dict[people[i]] > av:
    print(people[i])
  i += 1
