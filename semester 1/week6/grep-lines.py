#!/usr/bin/env python3

import sys

pattern = sys.argv[1:][0]
s = input()

while s != "end":
  i = len(pattern)

  while i < len(s) and s[i - len(pattern):i] != pattern:
    i += 1

  if s[i - len(pattern):i] == pattern:
    print(s)
  s = input()
