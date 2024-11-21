#!/usr/bin/env python3

import sys

file_name = sys.argv[1]
words = sys.argv[2:]

i = 0
with open(file_name, "w") as f:
  while i < len(words):
    f.write(words[i] + "\n")
    i += 1
