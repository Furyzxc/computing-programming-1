#!/usr/bin/env python3

import sys

vowels = "aeiouAEIOU"

dictionary = {}
i = 0

while i < len(vowels):
  dictionary[vowels[i]] = True
  i += 1

line = sys.stdin.readline()
count = 0
while line:
  i = 0
  while i < len(line):
    if line[i] in dictionary:
      count += 1
    i += 1
  line = sys.stdin.readline()
print(count)
