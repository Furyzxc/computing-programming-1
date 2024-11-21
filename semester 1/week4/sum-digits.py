#!/usr/bin/env python3

str = input()

i = 0
count = 0

while i < len(str):
  count += int(str[i])
  i += 1

print(count)
