#!/usr/bin/env python3

import sys

fruits = ["apple", "pear", "orange", "banana", "cherry"]

word = sys.stdin.readline().rstrip()

while word != "":
  if word in fruits:
    print(word)
  word = sys.stdin.readline().rstrip()
