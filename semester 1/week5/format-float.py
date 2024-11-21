#!/usr/bin/env python3

s = input()
i = 0

if s[0] == ".":
  print("0" + s)

elif s[-1] == ".":
  print(s + "0")

elif 1 < len(s) and s[0] == "-" and s[1] == ".":
  print("-0" + s[1::])

else:
  while i < len(s) and s[i] != ".":
    i += 1

  if i == len(s):
    print(s + ".0")
  else:
    print(s)
