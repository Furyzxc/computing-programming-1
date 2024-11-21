#!/usr/bin/env python3

prev = int(input())

while prev != 0:
  curr = int(input())
  if curr != 0:
    if curr > prev:
      print("higher")
    elif curr == prev:
      print("equal")
    else:
      print("lower")

  prev = curr
