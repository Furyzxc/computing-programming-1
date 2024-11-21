#!/usr/bin/env python3

arr = []

s = input()

i = 0

while i < 10:
  arr.append(0)
  i += 1

while s != "end":
  arr[int(s)] += 1
  s = input()

i = 0

while i < len(arr):
  print(i, arr[i] * "*")
  i += 1
