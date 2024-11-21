#!/usr/bin/env python3

import sys

args_words = sys.argv[1:]
stdin_words = sys.stdin.read().split()

i = 0
while i < len(stdin_words):
  word = stdin_words[i]
  if word in args_words:
    print(len(word) * "*")
  else:
    print(word)
  i += 1
