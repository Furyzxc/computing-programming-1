#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
  half = n // 2 + 1
  space = half - i - 1
  if space < 0:
    space = -space
  star = n - space * 2
  print(" " * space + "*" * star)
  i += 1
