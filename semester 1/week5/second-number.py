#!/usr/bin/env python3

s = input()

startIndex = -1
finishIndex = -1

a = -1
b = -1

i = 0

while i < len(s):
  if "0" <= s[i] <= "9" and startIndex == -1:
    startIndex = i
    finishIndex = startIndex
    while "0" <= s[finishIndex] <= "9":
      finishIndex += 1
  i += 1


while finishIndex < len(s) and startIndex != -1:
  if "0" <= s[finishIndex] <= "9" and a == -1:
    a = finishIndex
    b = a
    while b < len(s) and "0" <= s[b] <= "9":
      b += 1
  finishIndex += 1

if a != -1:
  print(s[a:b], a)
