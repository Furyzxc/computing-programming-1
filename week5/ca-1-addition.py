#!/usr/bin/env python3

s = input()

i = 0

while i < len(s) and s[i] != " ":
  i += 1

first = s[0:i]

j = i + 1

while j < len(s) and s[j] != " ":
  j += 1

second = s[i + 1:j]

third = s[j + 1:len(s)]

total = int(first) + int(second) + int(third)

print(total)
