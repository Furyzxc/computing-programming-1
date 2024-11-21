#!/usr/bin/env python3

arr = []
s = input()

while s != "end":
  arr += [int(s)]
  s = input()

i = 0

while i < len(arr):
  j = i
  while j < len(arr):
    if arr[i] > arr[j]:
      arr[i], arr[j] = arr[j], arr[i]
    j += 1

  i += 1

median = arr[i // 2]

print(median)
