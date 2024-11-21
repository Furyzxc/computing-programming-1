#!/usr/bin/env python3

curr = int(input())

count = 0
while count != 1:
  next = int(input())
  if curr % 2 == 0:
    if next == curr // 2:
      print(curr, next)
      count = 1
  else:
    if next == 3 * curr + 1:
      print(curr, next)
      count = 1
  curr = next
