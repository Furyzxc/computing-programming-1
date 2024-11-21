#!/usr/bin/env python3

dict = {}

intersection = {}
with open("a.txt") as f:
  words = f.read().split()

  i = 0

  while i < len(words):
    if words[i] not in dict:
      dict[words[i]] = True
    i += 1

with open("b.txt") as f:
  words = f.read().split()

  i = 0

  while i < len(words):
    if words[i] in dict:
      intersection[words[i]] = True
    i += 1

for word in intersection:
  print(word)
