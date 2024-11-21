#!/usr/bin/env python3

import sys

dict = {}
line = sys.stdin.readline()

while line:
  s = line.strip()

  file = s.split("/")
  user = file[0]

  if user not in dict:
    dict[user] = {}
  task = ".".join(file[1].split(".")[0:2])
  state = file[1].split(".")[-1]

  dict[user][task] = state

  line = sys.stdin.readline()

for user in dict:
  correct = 0
  i = 0
  data = dict[user]

  for file in data:
    if data[file] == "correct":
      correct += 1
    i += 1
  print(user + " " + str(correct))
