#!/usr/bin/env python3

import sys

file_name = sys.argv[1]

with open(file_name) as f:
  next_file = f.read().strip()

with open(next_file) as f:
  content = f.read().strip()
  print(content)
