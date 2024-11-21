#!/usr/bin/env python3

n = int(input())
res = ""

string = "abcdef"

while n != 0:
  num = (n - (n // 16) * 16) % 16

  n = n // 16
  if num > 9:
    num = string[num - 10]

  res += str(num)

print(res[::-1])
