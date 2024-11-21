#!/usr/bin/env python3

n = input()
i = 0
sum = 0

while i < len(n):
  sum += int(n[len(n) - i - 1]) * 2 ** i
  i += 1

print(sum)
