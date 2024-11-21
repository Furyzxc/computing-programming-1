#!/usr/bin/env python3

import sys
args = sys.argv[1:]          # Skip the first element in sys.argv.
print("echo.py")           # It's the script nam't care about.
i = 0
while i < len(args):
   print(args[i])
   i = i + 1
