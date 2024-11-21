#!/usr/bin/env python3

import sys

files = sys.argv[1:]

f1 = open(files[0])
f2 = open(files[1])

line = 0
i = 0
text1 = f1.readline()
text2 = f2.readline()

while text1 == text2 and text1 != "":
  line += 1
  text1 = f1.readline()
  text2 = f2.readline()

if text1 != text2:
  while i < len(text1) and i < len(text2) and text1[i] == text2[i]:
    i += 1
  print(line, i)
f1.close()
f2.close()
