#!/usr/bin/env python3

import sys              # import the sys module


args = sys.argv[1:]     # strip off the script name

i = 0

while i < len(args):
  print(args[i])
  i += 1
