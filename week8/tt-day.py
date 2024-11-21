#!/usr/bin/env python3

s = input()
arr = []

while s != "end":
  arr.append(s)
  s = input()

day = input()

i = 0
while i < len(arr):
  if arr[i].split()[0] == day:
    print(arr[i])
  i += 1
