#!/usr/bin/env python3

word = input()
flag = True
count = "a"
while word != "end":
  i = 0
  n = len(word)
  while i < n:
    if word[i] < count:
      flag = False
    count = word[i]
    i += 1

  if flag:
    print(word)
  flag = True
  count = "a"
  word = input()
