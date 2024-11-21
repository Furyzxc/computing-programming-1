#!/usr/bin/env python3

import sys

line = sys.stdin.readline()

brackets = {
  "(": ")",
  "[": "]",
  "{": "}"
}

line_index = 0

while line:
  stack = []
  start_indexes = []
  s = line.strip()

  i = 0
  while i < len(s):
    char = s[i]

    if char == "(" or char == "{" or char == "[":
      stack.append(char)
      start_indexes.append(i)
    elif char == ")" or char == "}" or char == "]":
      if len(stack) > 0:
        node = stack.pop()

        if brackets[node] != char:
          stack.append(node)
          stack.append(node)
          start_indexes.append(i)
          i = len(s)
      else:
        print(line_index, i)
        i = len(s)
    i += 1
  if len(stack) == 1:
    print(line_index, len(s))
  elif len(stack) != 0:
    print(line_index, start_indexes[-1])

  line = sys.stdin.readline()
  line_index += 1
