#!/usr/bin/env python3

arr = []

s = input()

while s != "end":
  arr.append(s)
  s = input()

i = 0

while i < len(arr):
  print(arr[len(arr) - i - 1])
  i += 1
