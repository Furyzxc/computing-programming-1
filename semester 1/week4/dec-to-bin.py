#!/usr/bin/env python3

n = int(input())
i = 0
res = ""

while n != 0:
  res += str((n - n // 2 * 2) % 2)
  n = n // 2

print(res[::-1])
