#!/usr/bin/env python3

arr = []
s = input()

while s != "end":
  arr += [s]
  s = input()

i = 0

while i < len(arr):
  j = i + 1

  while j < len(arr):
    if arr[i][6:8] > arr[j][6:8]:
      arr[i], arr[j] = arr[j], arr[i]
    elif arr[i][6:8] == arr[j][6:8]:
      if arr[i][3:5] > arr[j][3:5]:
        arr[i], arr[j] = arr[j], arr[i]
      elif arr[i][3:5] == arr[j][3:5]:
        if arr[i][0:2] > arr[j][0:2]:
          arr[i], arr[j] = arr[j], arr[i]
    j += 1
  i += 1

i = 0

while i < len(arr):
  print(arr[i][9:])
  i += 1
