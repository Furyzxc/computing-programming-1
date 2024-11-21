#!/usr/bin/env python3

import sys

args = sys.argv[1:]

i = 0
count = 0

while i < len(args):
  count += int(args[i])
  i += 1

print(count)
