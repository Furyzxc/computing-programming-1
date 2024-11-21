#!/usr/bin/env python3

import sys

file = sys.argv[1]

with open(file) as f:
  next_file = f.read().strip()

with open(next_file) as f:
  content = f.read().strip()
  print(content)
