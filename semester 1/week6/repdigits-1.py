#!/usr/bin/env python3

n = int(input())
i = 0

while i < n:
  s = input()
  j = 1
  while j < len(s) and s[j] == s[j - 1]:
    j += 1

  if j == len(s):
    print(s)
  i += 1
