#!/usr/bin/env python3

arr = []

s = input()
smallest = s
j = 0
i = 0
while s != "end":
  arr += [int(s)]
  i += 1
  if int(s) < int(smallest):
    smallest = s
    j = i - 1
  s = input()

print(j)
