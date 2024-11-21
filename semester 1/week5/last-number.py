#!/usr/bin/env python3

s = input()

n = -1

i = 0
while i < len(s):
  if "0" <= s[i] <= "9":
    n = s[i]
  i += 1

flag = True
res = ""
if n != -1:
  j = len(s)
  while j >= 0:
    if j < len(s) and "0" <= s[j] <= "9" and flag:
      res += s[j]
      if j < len(s) and not ("0" <= s[j - 1] <= "9"):
        flag = False
    j -= 1

  print(res[::-1])
