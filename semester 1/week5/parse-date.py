#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and s[i] != " ":
  i += 1

day = s[:i]

j = i + 1

while j < len(s) and s[j] != " ":
  j += 1

date = s[i + 1:j]

c = j + 1

while c < len(s) and s[c:c + 2] != ", ":
  c += 1

month = s[j + 1:c]

year = s[c + 2:len(s)]

print(month, date + ",", year, "(" + day + ")")
