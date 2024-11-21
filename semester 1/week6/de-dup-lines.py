#!/usr/bin/env python3

arr = []

s = input()

while s != "end":
  i = 0
  while i < len(arr) and arr[i] != s:
    i += 1

  if len(arr) == i:
    print(s)
    arr.append(s)

  s = input()
