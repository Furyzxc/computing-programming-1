#!/usr/bin/env python3

import sys

dict = {}
uploads = sys.stdin.readline()

while uploads != "":
  arr = uploads.strip().split(".")
  dict[arr[0] + "." + arr[1]] = arr[2]
  uploads = sys.stdin.readline()

i = 0
for word in dict:
  if dict[word] == "correct":
    print(word)
