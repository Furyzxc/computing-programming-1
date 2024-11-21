#!/usr/bin/env python3

s = input()

startIndex = -1
finishIndex = -1

i = 0

while i < len(s):
  if "A" <= s[i] <= "Z" and startIndex == -1:
    startIndex = i
    finishIndex = startIndex
    while finishIndex < len(s) and "A" <= s[finishIndex] <= "Z":
      finishIndex += 1
  i += 1

if startIndex != -1:
  print(s[startIndex:finishIndex], startIndex)
