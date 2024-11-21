#!/usr/bin/env python3

import sys

s = sys.stdin.readline()

while s != "":
  print(s.split("/")[-1][:-1])
  s = sys.stdin.readline()
