#!/usr/bin/env python3

s = input()

i = 0
j = len(s) - 1

while i < len(s) and s[i] == s[j]:
  i += 1
  j -= 1

if i == len(s):
  print("palindrome")
