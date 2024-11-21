#!/usr/bin/env python3

s = int(input())

num = "0123456789abcdef"
res = ""

while s != 0:
  rem = s - s // 16 * 16
  s = s // 16
  res += str(num[rem])

res = res[::-1]
i = 0

letters = "abcdef"

while i < len(res) and res[i] not in letters:
  i += 1

if i < len(res):
  print(res[i])
