#!/usr/bin/env python3

arr = []

s = input()
smallest = s
while s != "end":
  arr += [int(s)]
  if int(s) < int(smallest):
    smallest = s
  s = input()

print(smallest)
