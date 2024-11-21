#!/usr/bin/env python3

import sys

words = sys.stdin.read().split()

dict = {}
i = 0

while i < len(words):
  word = words[i]
  if word not in dict:
    dict[word] = True
  else:
    dict[word] = False
  i += 1

for word in dict:
  if dict[word]:
    print(word)
