#!/usr/bin/env python3

arr = []
s = input()

while s != "end":
  arr += [int(s)]
  s = input()

i = 0

while i < len(arr):
  j = i + 1
  while j < len(arr):
    if arr[i] > arr[j]:
      arr[i], arr[j], = arr[j], arr[i]
    j += 1
  i += 1

max = 500
current = 0
i = 0

while i < len(arr) and current + arr[i + 1] < max:
  current += arr[i]
  i += 1

print(i, current)
