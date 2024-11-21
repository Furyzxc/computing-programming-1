#!/usr/bin/env python3

s = input()

startIndex = -1
finishIndex = -1

i = 0

while i < len(s):
  if "0" <= s[i] <= "9" and startIndex == -1:
    startIndex = i
    finishIndex = startIndex
    while "0" <= s[finishIndex] <= "9":
      finishIndex += 1
  i += 1

if startIndex != -1:
  print(s[startIndex:finishIndex], startIndex)
