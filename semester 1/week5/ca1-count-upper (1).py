#!/usr/bin/env python3

s = input()
i = 0
count = 0

while i < len(s):
  if "A" <= s[i] <= "Z":
    count += 1
  i += 1

print(count)
