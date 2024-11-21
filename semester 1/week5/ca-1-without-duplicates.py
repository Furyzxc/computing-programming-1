#!/usr/bin/env python3

i = 1

prev = int(input())
print(prev)

while i < 10:
  curr = int(input())

  if curr != prev:
    print(curr)

  prev = curr
  i += 1
