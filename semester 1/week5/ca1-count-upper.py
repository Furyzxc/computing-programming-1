#!/usr/bin/env python3

s = int(input())
i = 0
count = 0

while i < len(s):
  if "A" <= s[i] and s[i] <= "Z":
    count += 1
print(count)
