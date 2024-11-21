#!/usr/bin/env python3

arr = []

s = input()

while s != "end":
  arr += [int(s)]
  s = input()

i = int(input()) + 1

smlst = i - 1

while i < len(arr):
  if arr[i] < arr[smlst]:
    smlst = i
  i += 1

print(smlst)
