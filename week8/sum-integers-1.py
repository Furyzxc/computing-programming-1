#!/usr/bin/env python3

import sys

a = sys.stdin.readline()
sum = 0
while a != "":
  sum += int(a)
  a = sys.stdin.readline()

print(sum)
