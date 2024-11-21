#!/usr/bin/env python3

s = input()
i = 0
j = 0
while i < len(s):
  if s[i] == ",":
    print(s[j:i])
    j = i + 1

  i += 1

while 1 != 1:
  pass
print(s[j:])
